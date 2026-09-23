from __future__ import annotations

import http.client
import tempfile
import threading
import unittest
from pathlib import Path

from scripts.preview_manual import ManualPreviewHandler
from http.server import ThreadingHTTPServer


class PreviewManualTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary_directory.cleanup)
        self.site = Path(self.temporary_directory.name)
        (self.site / "assets").mkdir()
        (self.site / "index.html").write_text("<main>Inicio</main>", encoding="utf-8")
        (self.site / "404.html").write_text("<main>No encontramos esta página</main>", encoding="utf-8")
        (self.site / "assets" / "extra.css").write_text("body {}", encoding="utf-8")
        handler = type("TestPreviewHandler", (ManualPreviewHandler,), {"site_directory": self.site, "base_path": "/manual/"})
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.addCleanup(self.close_server)

    def close_server(self) -> None:
        self.server.shutdown()
        self.thread.join()
        self.server.server_close()

    def request(self, path: str) -> tuple[int, str, str]:
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port)
        connection.request("GET", path)
        response = connection.getresponse()
        body = response.read().decode("utf-8")
        content_type = response.getheader("Content-Type", "")
        connection.close()
        return response.status, body, content_type

    def test_serves_the_manual_only_under_its_base_path(self) -> None:
        self.assertEqual((200, "<main>Inicio</main>", "text/html; charset=utf-8"), self.request("/manual/"))
        self.assertEqual(404, self.request("/")[0])

    def test_unknown_manual_route_returns_custom_404_with_http_404(self) -> None:
        status, body, _ = self.request("/manual/no-existe/")
        self.assertEqual(404, status)
        self.assertIn("No encontramos esta página", body)

    def test_serves_assets_and_rejects_path_traversal(self) -> None:
        status, body, content_type = self.request("/manual/assets/extra.css")
        self.assertEqual(200, status)
        self.assertEqual("body {}", body)
        self.assertIn("text/css", content_type)
        self.assertEqual(404, self.request("/manual/%2e%2e/index.html")[0])
