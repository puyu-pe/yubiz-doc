"""Serve a built manual from loopback under an explicit base path."""

from __future__ import annotations

import argparse
import mimetypes
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


class ManualPreviewHandler(BaseHTTPRequestHandler):
    """Serve static files without allowing a route to escape the site directory."""

    site_directory = Path(".build/site")
    base_path = "/manual/"

    def do_GET(self) -> None:  # noqa: N802 - required by BaseHTTPRequestHandler
        request_path = urlsplit(self.path).path
        if not request_path.startswith(self.base_path):
            self.send_not_found()
            return
        relative = unquote(request_path[len(self.base_path) :])
        if relative.startswith("/") or ".." in Path(relative).parts:
            self.send_not_found()
            return
        target = self.site_directory / relative
        if target.is_dir():
            target /= "index.html"
        if not target.is_file() or not target.resolve().is_relative_to(self.site_directory.resolve()):
            self.send_not_found()
            return
        content_type = mimetypes.guess_type(str(target))[0] or "application/octet-stream"
        if content_type == "text/html":
            content_type = "text/html; charset=utf-8"
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(target.stat().st_size))
        self.end_headers()
        self.wfile.write(target.read_bytes())

    def send_not_found(self) -> None:
        page = self.site_directory / "404.html"
        body = page.read_bytes() if page.is_file() else b"<main>No encontramos esta pagina</main>"
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path(".build/site"))
    parser.add_argument("--base-path", default="/manual/")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    base_path = "/" + args.base_path.strip("/") + "/"
    if args.host != "127.0.0.1":
        parser.error("preview must bind only to 127.0.0.1")
    if not args.site_dir.is_dir():
        parser.error(f"site directory does not exist: {args.site_dir}")
    handler = type(
        "ConfiguredManualPreviewHandler",
        (ManualPreviewHandler,),
        {"site_directory": args.site_dir.resolve(), "base_path": base_path},
    )
    server = ThreadingHTTPServer((args.host, args.port), handler)
    print(f"Serving {args.site_dir} at http://{args.host}:{args.port}{base_path}", flush=True)
    try:
        server.serve_forever()
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
