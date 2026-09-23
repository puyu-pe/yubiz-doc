import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.build_manual import build, checked_url, sha256_file


class BuildManualTests(unittest.TestCase):
    def fixture_root(self, directory: Path) -> Path:
        root = directory / "manual"
        (root / "docs").mkdir(parents=True)
        (root / "overrides").mkdir()
        (root / "docs" / "index.md").write_text("# Manual\n", encoding="utf-8")
        (root / "overrides" / "main.html").write_text("{% extends 'base.html' %}\n", encoding="utf-8")
        (root / "mkdocs.yml").write_text(
            "site_name: Manual\nsite_url: https://docs.example.test/manual/\ndocs_dir: docs\nsite_dir: site\ntheme:\n  name: material\n  custom_dir: overrides\n",
            encoding="utf-8",
        )
        return root

    def test_build_is_deterministic_and_lists_every_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self.fixture_root(Path(temporary))
            first = build(root, "https://docs.example.test/manual/", ".build/out/one", 1_700_000_000, "a" * 40)
            second = build(root, "https://docs.example.test/manual/", ".build/out/two", 1_700_000_000, "a" * 40)
            self.assertEqual(first["manifest_sha256"], second["manifest_sha256"])
            self.assertEqual(sha256_file(Path(first["archive"])), sha256_file(Path(second["archive"])))
            manifest = json.loads(Path(first["manifest"]).read_text(encoding="utf-8"))
            self.assertEqual(sorted(item["path"] for item in manifest["entries"]), [item["path"] for item in manifest["entries"]])
            self.assertTrue(any(item["path"] == "sitemap.xml.gz" for item in manifest["entries"]))
            search = Path(first["archive"]).parent / "site" / "search" / "search_index.json"
            self.assertNotIn("source_reviewed_draft", search.read_text(encoding="utf-8"))

    def test_manifest_and_archive_use_posix_lexicographic_path_order(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self.fixture_root(Path(temporary))
            for relative in (
                "reportes/index.html",
                "reportes-especializados/index.html",
                "reportes/a.html",
                "zeta/index.html",
            ):
                path = root / "docs" / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text("page\n", encoding="utf-8")
            result = build(root, "https://docs.example.test/manual/", ".build/out", 1_700_000_000, "a" * 40)
            manifest = json.loads(Path(result["manifest"]).read_text(encoding="utf-8"))
            paths = [entry["path"] for entry in manifest["entries"]]
            self.assertLess(paths.index("reportes-especializados/index.html"), paths.index("reportes/index.html"))
            import tarfile
            with tarfile.open(result["archive"], "r:gz") as archive:
                names = [member.name for member in archive.getmembers() if member.name != "manifest.json"]
            self.assertEqual(paths, names)

    def test_rejects_unsafe_output_and_site_url(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self.fixture_root(Path(temporary))
            with self.assertRaisesRegex(ValueError, "output"):
                build(root, "https://docs.example.test/manual/", "../outside", 1_700_000_000, "a" * 40)
            with self.assertRaisesRegex(ValueError, "output"):
                build(root, "https://docs.example.test/manual/", ".build", 1_700_000_000, "a" * 40)
            with self.assertRaisesRegex(ValueError, "site URL"):
                build(root, "http://docs.example.test/manual/", ".build/out", 1_700_000_000, "a" * 40)

    def test_rejects_missing_configuration(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            with self.assertRaisesRegex(ValueError, "mkdocs.yml"):
                build(root, "https://docs.example.test/manual/", ".build/out", 1_700_000_000, "a" * 40)

    def test_normalizes_only_safe_canonical_https_urls(self) -> None:
        self.assertEqual("https://docs.example.test/manual/", checked_url("HTTPS://DOCS.EXAMPLE.TEST/manual/"))
        for value in ("https://user@docs.example.test/manual/", "https://docs.example.test/manual/?x=1", "https://docs.example.test/manual/#part", "https://docs.example.test/../manual/", "https://docs.example.test//manual/"):
            with self.assertRaisesRegex(ValueError, "site URL"):
                checked_url(value)
