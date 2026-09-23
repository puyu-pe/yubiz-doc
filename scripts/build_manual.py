"""Build a deterministic local release artifact without editing mkdocs.yml."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
import shutil
import stat
import subprocess
import tarfile
import tempfile
import re
from pathlib import Path
from urllib.parse import urlparse, urlunparse

import yaml


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_output(root: Path, output: str) -> Path:
    candidate = (root / output).resolve()
    build_root = (root / ".build").resolve()
    if candidate == build_root or not candidate.is_relative_to(build_root):
        raise ValueError("output must be under .build")
    return candidate


def checked_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme.lower() != "https" or not parsed.hostname or parsed.username or parsed.password or parsed.params or parsed.query or parsed.fragment or not parsed.path.endswith("/") or ".." in parsed.path.split("/") or "//" in parsed.path:
        raise ValueError("site URL must be an absolute HTTPS URL ending in /")
    netloc = parsed.hostname.lower() + (f":{parsed.port}" if parsed.port else "")
    return urlunparse(("https", netloc, parsed.path, "", "", ""))


def base_path(site_url: str) -> str:
    return urlparse(site_url).path


def normalize_gzip(path: Path, epoch: int) -> None:
    with gzip.open(path, "rb") as source:
        payload = source.read()
    with path.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=epoch) as target:
            target.write(payload)


def normalize_tree(site: Path, epoch: int) -> list[dict[str, object]]:
    entries = []
    files = (item for item in site.rglob("*") if item.is_file())
    for path in sorted(files, key=lambda item: item.relative_to(site).as_posix()):
        if path.suffix == ".gz":
            normalize_gzip(path, epoch)
        mode = 0o755 if path.stat().st_mode & stat.S_IXUSR else 0o644
        path.chmod(mode)
        os.utime(path, (epoch, epoch))
        entries.append({"path": path.relative_to(site).as_posix(), "mode": mode, "size": path.stat().st_size, "sha256": sha256_file(path)})
    return entries


def write_archive(site: Path, manifest: Path, archive: Path, epoch: int) -> None:
    with archive.open("wb") as raw:
        with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=epoch) as compressed:
            with tarfile.open(fileobj=compressed, mode="w") as tar:
                files = (item for item in site.rglob("*") if item.is_file())
                ordered = sorted(files, key=lambda item: item.relative_to(site).as_posix())
                for source, name in [(manifest, "manifest.json"), *[(item, item.relative_to(site).as_posix()) for item in ordered]]:
                    info = tar.gettarinfo(str(source), arcname=name)
                    info.uid = info.gid = 0
                    info.uname = info.gname = ""
                    info.mtime = epoch
                    with source.open("rb") as handle:
                        tar.addfile(info, handle)


def build(root: Path, site_url: str, output: str, source_date_epoch: int, source_commit: str) -> dict[str, str]:
    root = root.resolve()
    config = root / "mkdocs.yml"
    if not config.is_file():
        raise ValueError("mkdocs.yml is required")
    site_url = checked_url(site_url)
    destination = checked_output(root, output)
    if destination.exists():
        shutil.rmtree(destination)
    destination.mkdir(parents=True)
    with tempfile.TemporaryDirectory(dir=destination) as temporary:
        generated_config = Path(temporary) / "mkdocs.yml"
        generated_site = destination / "site"
        configuration = yaml.safe_load(config.read_text(encoding="utf-8"))
        configuration.update({"site_url": site_url, "docs_dir": str(root / "docs"), "site_dir": str(generated_site)})
        configuration.setdefault("theme", {})["custom_dir"] = str(root / "overrides")
        generated_config.write_text(yaml.safe_dump(configuration, allow_unicode=True, sort_keys=False), encoding="utf-8")
        subprocess.run([os.sys.executable, "-m", "mkdocs", "build", "--strict", "--clean", "--config-file", str(generated_config)], check=True, cwd=root)
    entries = normalize_tree(generated_site, source_date_epoch)
    manifest = destination / "manifest.json"
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("source commit must be a full 40-character lowercase SHA")
    manifest.write_text(json.dumps({"schema": "manual-release-manifest/v1", "source_commit": source_commit, "site_url": site_url, "base_path": base_path(site_url), "source_date_epoch": source_date_epoch, "entries": entries}, indent=2) + "\n", encoding="utf-8")
    archive = destination / "manual.tar.gz"
    write_archive(generated_site, manifest, archive, source_date_epoch)
    return {"archive": str(archive), "manifest": str(manifest), "manifest_sha256": sha256_file(manifest)}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--site-url")
    parser.add_argument("--deployment-target", type=Path)
    parser.add_argument("--output", default=".build/release")
    parser.add_argument("--source-date-epoch", type=int, required=True)
    parser.add_argument("--source-commit", required=True)
    args = parser.parse_args()
    if bool(args.site_url) == bool(args.deployment_target):
        parser.error("choose exactly one of --site-url or --deployment-target")
    if args.deployment_target:
        from publish_manual import load_target
        args.site_url = load_target(args.deployment_target)["site_url"]
    del args.deployment_target
    print(json.dumps(build(**vars(args)), sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
