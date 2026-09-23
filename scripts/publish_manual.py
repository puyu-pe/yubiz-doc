"""Fail-closed publication planning and optional isolated static upload."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import subprocess
import tarfile
import tempfile
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import yaml


SHA = re.compile(r"^[0-9a-f]{40}$")
SAFE_REMOTE = re.compile(r"^/[A-Za-z0-9._/-]+$")
SAFE_NAME = re.compile(r"^[A-Za-z0-9._-]+$")
SAFE_HOST = re.compile(r"^[A-Za-z0-9.-]+$")


class GuardError(ValueError):
    """A publication prerequisite was not proven."""


def canonical_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme.lower() != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.params or parsed.query or parsed.fragment or not parsed.path.endswith("/") or ".." in parsed.path.split("/") or "//" in parsed.path:
        raise GuardError("site URL and base path are inconsistent")
    return urlunparse(("https", parsed.hostname.lower() + (f":{parsed.port}" if parsed.port else ""), parsed.path, "", "", ""))


def canonical_target_root(value: str) -> str:
    if (
        not SAFE_REMOTE.fullmatch(value)
        or value == "/"
        or "//" in value
        or value.endswith("/")
        or any(part in {".", ".."} for part in value.split("/"))
        or any(character.isspace() or ord(character) < 32 for character in value)
    ):
        raise GuardError("target root or marker is unsafe")
    return value


def load_target(path: Path) -> dict[str, str]:
    try:
        target = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        raise GuardError("deployment target cannot be read") from error
    if not isinstance(target, dict):
        raise GuardError("deployment target must be a mapping")
    required = ("activation", "verification_state", "site_url", "base_path", "host", "user", "port", "target_root", "marker", "marker_value", "known_hosts_secret", "key_secret")
    if any(not isinstance(target.get(key), str) or not target[key] for key in required):
        raise GuardError("deployment target has missing required configuration")
    if target["activation"] != "verified" or target["verification_state"] != "verified":
        raise GuardError("publication is blocked until activation and verification are verified")
    target["site_url"] = canonical_url(target["site_url"])
    if target["base_path"] != urlparse(target["site_url"]).path:
        raise GuardError("site URL must end with the configured base path")
    if not target["port"].isdigit() or not 1 <= int(target["port"]) <= 65535:
        raise GuardError("port must be in the SSH range")
    if not SAFE_HOST.fullmatch(target["host"]) or not SAFE_NAME.fullmatch(target["user"]):
        raise GuardError("host or user is unsafe")
    target["target_root"] = canonical_target_root(target["target_root"])
    if not SAFE_NAME.fullmatch(target["marker"]) or target["marker_value"] != "manual-publication-root/v1":
        raise GuardError("target root or marker is unsafe")
    if not all(SAFE_NAME.fullmatch(target[key]) for key in ("known_hosts_secret", "key_secret")):
        raise GuardError("secret names are unsafe")
    return target


def checked_sha(value: str) -> str:
    if not SHA.fullmatch(value):
        raise GuardError("publication requires a full 40-character lowercase SHA")
    return value


def checked_reviewed_main(root: Path, sha: str) -> None:
    if not (root / ".git").exists():
        raise GuardError("local repository identity is unavailable")
    expected_origin = "git@github.com:puyu-pe/yubiz-doc.git"
    commands = (["git", "-C", str(root), "remote", "get-url", "origin"], ["git", "-C", str(root), "rev-parse", "--verify", f"{sha}^{{commit}}"], ["git", "-C", str(root), "merge-base", "--is-ancestor", sha, "origin/main"])
    for command in commands:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        if result.returncode:
            raise GuardError("reviewed origin/main cannot be verified locally; an unborn or incomplete repository cannot activate publication")
        if command[3:5] == ["remote", "get-url"] and result.stdout.strip() != expected_origin:
            raise GuardError("repository origin does not match the reviewed publication identity")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_artifact(directory: Path, sha: str, target: dict[str, str]) -> dict[str, object]:
    manifest_path, archive_path = directory / "manifest.json", directory / "manual.tar.gz"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise GuardError("release manifest is missing or invalid") from error
    if manifest.get("schema") != "manual-release-manifest/v1" or manifest.get("source_commit") != sha or not isinstance(manifest.get("entries"), list):
        raise GuardError("release manifest is not bound to the requested source SHA")
    if manifest.get("site_url") != target["site_url"] or manifest.get("base_path") != target["base_path"]:
        raise GuardError("release manifest does not match the verified canonical target")
    seen: set[str] = set()
    for entry in manifest["entries"]:
        if not isinstance(entry, dict) or not isinstance(entry.get("path"), str):
            raise GuardError("release manifest contains an unsafe path")
        relative = Path(entry["path"])
        if relative.is_absolute() or ".." in relative.parts or entry["path"] in seen:
            raise GuardError("release manifest contains a duplicate or escaping path")
        seen.add(entry["path"])
        file = directory / "site" / relative
        if file.is_symlink() or not file.is_file() or entry.get("mode") != 0o644 or entry.get("size") != file.stat().st_size or entry.get("sha256") != digest(file):
            raise GuardError("release artifact integrity check failed")
    try:
        with tarfile.open(archive_path, "r:gz") as archive:
            members = archive.getmembers()
            names = [member.name for member in members]
            if any(member.issym() or member.islnk() or member.mode & 0o111 for member in members) or len(names) != len(set(names)) or set(names) != {"manifest.json", *seen}:
                raise GuardError("release archive contains unsafe payloads")
            expected = {entry["path"]: entry["sha256"] for entry in manifest["entries"]}
            for member in members:
                if member.name != "manifest.json" and hashlib.sha256(archive.extractfile(member).read()).hexdigest() != expected[member.name]:
                    raise GuardError("release archive integrity check failed")
    except (OSError, tarfile.TarError) as error:
        raise GuardError("release archive is missing or invalid") from error
    return {"archive": archive_path, "manifest_sha256": digest(manifest_path), "archive_sha256": digest(archive_path)}


def remote_check_command(target: dict[str, str], sha: str) -> str:
    root, marker = target["target_root"], target["marker"]
    release = f"{root}/releases/{sha}"
    return " && ".join((f"test -d {shlex.quote(root)}", f"test ! -L {shlex.quote(root)}", f"test -d {shlex.quote(root + '/releases')}", f"test ! -L {shlex.quote(root + '/releases')}", f"test -f {shlex.quote(root + '/' + marker)}", f"test \"$(cat -- {shlex.quote(root + '/' + marker)})\" = {shlex.quote(target['marker_value'])}", f"test ! -e {shlex.quote(release)}"))


def plan(root: Path, target_path: Path, artifact_dir: Path, sha: str) -> dict[str, str]:
    sha = checked_sha(sha)
    target = load_target(target_path)
    artifact = checked_artifact(artifact_dir.resolve(), sha, target)
    checked_reviewed_main(root.resolve(), sha)
    return {"release": f"{target['target_root']}/releases/{sha}", "remote_check": remote_check_command(target, sha), "manifest_sha256": str(artifact["manifest_sha256"]), "archive_sha256": str(artifact["archive_sha256"])}


def upload(root: Path, target_path: Path, artifact_dir: Path, sha: str) -> dict[str, str]:
    release_plan = plan(root, target_path, artifact_dir, sha)
    target = load_target(target_path)
    known_hosts, key = os.environ.get(target["known_hosts_secret"]), os.environ.get(target["key_secret"])
    if not known_hosts or not key:
        raise GuardError("required SSH secret values are unavailable")
    with tempfile.TemporaryDirectory() as temporary:
        directory = Path(temporary)
        known = directory / "known_hosts"; known.write_text(known_hosts, encoding="utf-8"); known.chmod(0o600)
        private = directory / "key"; private.write_text(key, encoding="utf-8"); private.chmod(0o600)
        ssh = ["ssh", "-i", str(private), "-o", "BatchMode=yes", "-o", "StrictHostKeyChecking=yes", "-o", f"UserKnownHostsFile={known}", "-p", target["port"], f"{target['user']}@{target['host']}"]
        subprocess.run([*ssh, release_plan["remote_check"] + f" && mkdir {shlex.quote(release_plan['release'])}"], check=True)
        transport = shlex.join(ssh[:-1])
        subprocess.run(["rsync", "-a", "-e", transport, "--chmod=Du=rwx,Dgo=rx,Fu=rw,Fgo=r", "--", str(artifact_dir / "site") + "/", f"{target['user']}@{target['host']}:{release_plan['release']}/"], check=True)
    return release_plan


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--target", type=Path, default=Path("documentation/deployment-target.yml"))
    parser.add_argument("--artifact-dir", type=Path, required=True)
    parser.add_argument("--sha", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--upload", action="store_true")
    args = parser.parse_args()
    if args.dry_run == args.upload:
        parser.error("choose exactly one of --dry-run or --upload")
    result = plan(args.root, args.target, args.artifact_dir, args.sha) if args.dry_run else upload(args.root, args.target, args.artifact_dir, args.sha)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except GuardError as error:
        print(f"publish guard: {error}", file=os.sys.stderr)
        raise SystemExit(2)
