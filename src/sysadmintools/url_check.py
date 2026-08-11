"""Check allowlisted HTTP(S) URLs without following redirects."""

from __future__ import annotations

import argparse
import json
import ssl
import sys
import time
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass
from urllib.parse import urlsplit


@dataclass(frozen=True, slots=True)
class URLResult:
    url: str
    ok: bool
    status: int | None
    elapsed_seconds: float
    bytes_sampled: int
    error: str | None = None


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        return None


def validate_url(url: str, allowed_hosts: set[str], allow_http: bool) -> str:
    parsed = urlsplit(url)
    allowed_schemes = {"https", "http"} if allow_http else {"https"}
    if parsed.scheme not in allowed_schemes:
        raise ValueError(f"scheme not allowed: {parsed.scheme!r}")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("credentials in URL are not allowed")
    hostname = (parsed.hostname or "").rstrip(".").lower()
    if hostname not in allowed_hosts:
        raise ValueError(f"host not allowlisted: {hostname!r}")
    if parsed.fragment:
        raise ValueError("URL fragments are not sent to servers and are not allowed")
    return url


def check_url(url: str, timeout: float, max_body: int = 4096) -> URLResult:
    context = ssl.create_default_context()
    opener = urllib.request.build_opener(
        NoRedirect(), urllib.request.HTTPSHandler(context=context)
    )
    request = urllib.request.Request(url, headers={"User-Agent": "sysadmin-url-check/0.1"})
    started = time.monotonic()
    try:
        with opener.open(request, timeout=timeout) as response:
            body = response.read(max_body)
            status = response.status
            ok = 200 <= status < 300
            return URLResult(url, ok, status, round(time.monotonic() - started, 4), len(body))
    except urllib.error.HTTPError as error:
        return URLResult(
            url,
            False,
            error.code,
            round(time.monotonic() - started, 4),
            0,
            f"HTTP {error.code}",
        )
    except (OSError, urllib.error.URLError, TimeoutError) as error:
        return URLResult(url, False, None, round(time.monotonic() - started, 4), 0, str(error))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("urls", nargs="+")
    parser.add_argument("--allow-host", action="append", required=True)
    parser.add_argument("--allow-http", action="store_true", help="permit plaintext HTTP")
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--json", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not 0.1 <= args.timeout <= 120.0:
        print("error: timeout must be from 0.1 to 120 seconds", file=sys.stderr)
        return 2
    allowed_hosts = {host.rstrip(".").lower() for host in args.allow_host}
    try:
        urls = [validate_url(url, allowed_hosts, args.allow_http) for url in args.urls]
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    results = [check_url(url, args.timeout) for url in urls]
    if args.json:
        print(json.dumps([asdict(result) for result in results], sort_keys=True))
    else:
        for result in results:
            print(
                f"{result.url}: ok={str(result.ok).lower()} status={result.status} "
                f"elapsed={result.elapsed_seconds:.4f}s sampled={result.bytes_sampled}"
            )
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
