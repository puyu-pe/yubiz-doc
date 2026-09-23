"""Create safe byte-level snapshots for selected manual files."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import stat
from pathlib import Path

BLOCKED_PARTS = {".git", ".build", "secrets"}


def line_count(data: bytes) -> int:
    return data.count(b"\n") + int(bool(data) and not data.endswith(b"\n"))


def safe_path(root: Path, relative: str) -> Path:
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts or BLOCKED_PARTS.intersection(path.parts):
        raise ValueError(f"unsafe path: {relative}")
    candidate = root / path
    if candidate.is_symlink() or not candidate.resolve().is_relative_to(root):
        raise ValueError(f"unsafe path: {relative}")
    return candidate


def safe_output(root: Path, output: Path) -> Path:
    resolved = output.resolve()
    build = (root / ".build").resolve()
    if not resolved.is_relative_to(build):
        raise ValueError("output must be under .build")
    return resolved


def file_entry(root: Path, relative: str) -> dict[str, object]:
    path = safe_path(root, relative)
    if not path.is_file():
        return {"path": relative, "exists": False, "mode": None, "size": 0, "line_count": 0, "sha256": None}
    data = path.read_bytes()
    return {
        "path": relative,
        "exists": True,
        "mode": stat.S_IMODE(path.stat().st_mode),
        "size": len(data),
        "line_count": line_count(data),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def snapshot(root: Path, output: Path, paths: list[str]) -> dict[str, object]:
    root = root.resolve()
    output = safe_output(root, output)
    entries = [file_entry(root, path) for path in paths]
    output.mkdir(parents=True, exist_ok=True)
    files = output / "files"
    for entry in entries:
        if entry["exists"]:
            source = safe_path(root, str(entry["path"]))
            destination = files / str(entry["path"])
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
    manifest = {"schema": "manual-snapshot/v1", "entries": entries}
    (output / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def diff(root: Path, snapshot_dir: Path) -> dict[str, object]:
    root = root.resolve()
    snapshot_dir = safe_output(root, snapshot_dir)
    manifest = json.loads((snapshot_dir / "manifest.json").read_text(encoding="utf-8"))
    changes: list[dict[str, str]] = []
    for before in manifest["entries"]:
        after = file_entry(root, before["path"])
        if not before["exists"] and after["exists"]:
            changes.append({"path": after["path"], "change": "new"})
        elif before["exists"] and not after["exists"]:
            changes.append({"path": before["path"], "change": "deleted"})
        elif before != after:
            changes.append({"path": after["path"], "change": "changed"})
    report = {"schema": "manual-snapshot-diff/v1", "changes": changes}
    (snapshot_dir / "diff.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=("snapshot", "diff"))
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--path", action="append", default=[])
    args = parser.parse_args()
    result = snapshot(args.root, args.output, args.path) if args.action == "snapshot" else diff(args.root, args.output)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
