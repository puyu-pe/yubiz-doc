from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from scripts.snapshot_manual import diff, snapshot


class SnapshotManualTests(unittest.TestCase):
    def test_snapshots_actual_bytes_mode_and_exact_selected_count(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".build").mkdir()
            source = root / "docs" / "known.md"
            source.parent.mkdir()
            source.write_bytes(b"uno\ndos\n")
            source.chmod(0o640)
            manifest = snapshot(root, root / ".build" / "before", ["docs/known.md", "scripts/new.py"])

            self.assertEqual(2, len(manifest["entries"]))
            self.assertEqual(8, manifest["entries"][0]["size"])
            self.assertEqual(2, manifest["entries"][0]["line_count"])
            self.assertEqual(0o640, manifest["entries"][0]["mode"])
            self.assertFalse(manifest["entries"][1]["exists"])
            self.assertEqual(b"uno\ndos\n", (root / ".build/before/files/docs/known.md").read_bytes())

    def test_diff_reports_new_changed_and_deleted(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".build").mkdir()
            for name, content in (("docs/changed.md", "before"), ("docs/deleted.md", "gone")):
                path = root / name
                path.parent.mkdir(exist_ok=True)
                path.write_text(content, encoding="utf-8")
            output = root / ".build" / "before"
            snapshot(root, output, ["docs/changed.md", "docs/deleted.md", "docs/new.md"])
            (root / "docs/changed.md").write_text("after", encoding="utf-8")
            (root / "docs/deleted.md").unlink()
            (root / "docs/new.md").write_text("new", encoding="utf-8")

            report = diff(root, output)

            self.assertEqual({"changed", "deleted", "new"}, {item["change"] for item in report["changes"]})

    def test_rejects_escape_symlink_and_non_build_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".build").mkdir()
            outside = root.parent / "outside-manual-snapshot.txt"
            outside.write_text("outside", encoding="utf-8")
            link = root / "docs" / "escape.md"
            link.parent.mkdir()
            link.symlink_to(outside)
            with self.assertRaises(ValueError):
                snapshot(root, root / ".build" / "before", ["../outside"])
            with self.assertRaises(ValueError):
                snapshot(root, root / ".build" / "before", ["docs/escape.md"])
            with self.assertRaises(ValueError):
                snapshot(root, root / "output", ["docs/escape.md"])

    def test_cli_exercises_snapshot(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".build").mkdir()
            path = root / "docs" / "known.md"
            path.parent.mkdir()
            path.write_text("known\n", encoding="utf-8")
            command = [
                os.environ.get("PYTHON", "python"), "scripts/snapshot_manual.py", "snapshot",
                "--root", str(root), "--output", str(root / ".build" / "before"), "--path", "docs/known.md",
            ]
            result = subprocess.run(command, cwd=Path(__file__).parent.parent, capture_output=True, text=True, check=False)
            self.assertEqual(0, result.returncode, result.stderr)
            self.assertEqual(1, len(json.loads(result.stdout)["entries"]))
