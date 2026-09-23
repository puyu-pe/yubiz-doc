from __future__ import annotations

import hashlib
import json
import tarfile
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.publish_manual import GuardError, checked_artifact, checked_sha, load_target, plan


SHA = "a" * 40


class PublishManualTests(unittest.TestCase):
    def target(self, directory: Path, **changes: str) -> Path:
        values = {"activation": "verified", "verification_state": "verified", "site_url": "https://docs.example.test/manual/", "base_path": "/manual/", "host": "docs.example.test", "user": "publisher", "port": "22", "target_root": "/srv/manual", "marker": ".manual-root", "marker_value": "manual-publication-root/v1", "known_hosts_secret": "PUBLISH_KNOWN_HOSTS", "key_secret": "PUBLISH_SSH_PRIVATE_KEY"}
        values.update(changes)
        path = directory / "target.yml"
        path.write_text(__import__("yaml").safe_dump(values), encoding="utf-8")
        return path

    def artifact(self, directory: Path, *, source: str = SHA, site_url: str = "https://docs.example.test/manual/") -> Path:
        site = directory / "artifact/site"; site.mkdir(parents=True)
        page = site / "index.html"; page.write_text("safe", encoding="utf-8")
        entry = {"path": "index.html", "mode": 0o644, "size": 4, "sha256": hashlib.sha256(b"safe").hexdigest()}
        manifest = {"schema": "manual-release-manifest/v1", "source_commit": source, "site_url": site_url, "base_path": "/manual/", "entries": [entry]}
        root = site.parent; (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        with tarfile.open(root / "manual.tar.gz", "w:gz") as archive:
            archive.add(root / "manifest.json", "manifest.json"); archive.add(page, "index.html")
        return root

    def test_default_blocked_config_prevents_git_or_network_checks(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "blocked.yml"
            target.write_text("activation: blocked\n", encoding="utf-8")
            with patch("scripts.publish_manual.subprocess.run") as run:
                with self.assertRaisesRegex(GuardError, "missing|required|blocked"):
                    plan(Path(temporary), target, Path(temporary), SHA)
            run.assert_not_called()

    def test_rejects_injection_paths_and_invalid_sha(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = self.target(Path(temporary), target_root="/srv/manual;rm")
            with self.assertRaisesRegex(GuardError, "unsafe"):
                load_target(target)
            target = self.target(Path(temporary), host="docs.example.test;rm")
            with self.assertRaisesRegex(GuardError, "host or user"):
                load_target(target)
        with self.assertRaisesRegex(GuardError, "40-character"):
            checked_sha("$(whoami)")

    def test_rejects_noncanonical_target_roots_before_git_or_network(self) -> None:
        invalid_roots = (
            "/srv/../manual", "/srv/./manual", "/srv//manual", "/srv/manual/",
            "/", " /srv/manual", "/srv/manual ", "/srv/manual\n",
            "/srv/manual;rm", "relative/manual", "//srv/manual",
        )
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / ".git").mkdir()
            artifact = self.artifact(directory)
            for root in invalid_roots:
                with self.subTest(target_root=repr(root)):
                    target = self.target(directory, target_root=root)
                    with patch("scripts.publish_manual.subprocess.run") as run:
                        with self.assertRaisesRegex(GuardError, "target root"):
                            plan(directory, target, artifact, SHA)
                    run.assert_not_called()
            self.assertEqual("/srv/manual", load_target(self.target(directory))["target_root"])

    def test_rejects_wrong_marker_and_never_accepts_secret_values_as_output(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = self.target(Path(temporary), marker_value="wrong")
            with self.assertRaisesRegex(GuardError, "target root or marker"):
                load_target(target)
            with self.assertRaisesRegex(GuardError, "cannot be read") as error:
                load_target(Path(temporary) / "absent.yml")
            self.assertNotIn("PUBLISH_SSH_PRIVATE_KEY", str(error.exception))

    def test_rejects_manifest_tamper_escape_and_executable_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = self.artifact(Path(temporary))
            (root / "site/index.html").write_text("tampered", encoding="utf-8")
            with self.assertRaisesRegex(GuardError, "integrity"):
                checked_artifact(root, SHA, load_target(self.target(Path(temporary))))
            root = self.artifact(Path(temporary) / "second")
            manifest = json.loads((root / "manifest.json").read_text(encoding="utf-8")); manifest["entries"][0]["path"] = "../escape"
            (root / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            with self.assertRaisesRegex(GuardError, "unsafe|escaping"):
                checked_artifact(root, SHA, load_target(self.target(Path(temporary) / "second")))

    def test_dry_run_success_is_a_plan_not_a_remote_action(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary); artifact = self.artifact(directory); target = self.target(directory)
            with patch("scripts.publish_manual.checked_reviewed_main") as reviewed:
                result = plan(directory, target, artifact, SHA)
            reviewed.assert_called_once()
            self.assertIn("releases/" + SHA, result["release"])
            self.assertNotIn("--delete", result["remote_check"])
            self.assertIn("manual-publication-root/v1", result["remote_check"])

    def test_prior_release_recovery_rechecks_artifact_and_reviewed_ref_without_activation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            (directory / ".git").mkdir()
            artifact = self.artifact(directory)
            target = self.target(directory)
            completed = __import__("subprocess").CompletedProcess
            with patch(
                "scripts.publish_manual.subprocess.run",
                side_effect=(
                    completed(["git"], 0, "git@github.com:puyu-pe/yubiz-doc.git\n", ""),
                    completed(["git"], 0, "", ""),
                    completed(["git"], 0, "", ""),
                ),
            ) as run:
                recovery = plan(directory, target, artifact, SHA)
            self.assertEqual(f"/srv/manual/releases/{SHA}", recovery["release"])
            self.assertEqual(3, run.call_count)
            self.assertTrue(all(call.args[0][0] == "git" for call in run.call_args_list))
            self.assertNotIn("--delete", recovery["remote_check"])
            self.assertNotIn("activate", recovery["remote_check"])

    def test_prior_release_recovery_refuses_mismatched_artifact_before_git(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            artifact = self.artifact(directory, source="b" * 40)
            target = self.target(directory)
            with patch("scripts.publish_manual.subprocess.run") as run:
                with self.assertRaisesRegex(GuardError, "requested source SHA"):
                    plan(directory, target, artifact, SHA)
            run.assert_not_called()

    def test_rejects_same_sha_artifact_for_a_different_canonical_target_before_git(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            artifact = self.artifact(directory, site_url="https://other.example.test/manual/")
            target = self.target(directory)
            with patch("scripts.publish_manual.checked_reviewed_main") as reviewed:
                with self.assertRaisesRegex(GuardError, "canonical target"):
                    plan(directory, target, artifact, SHA)
            reviewed.assert_not_called()
