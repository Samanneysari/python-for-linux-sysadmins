"""Collect a small, unprivileged Linux inventory as JSON."""

from __future__ import annotations

import argparse
import json
import platform
import shlex
import shutil
import socket
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def parse_os_release(path: Path = Path("/etc/os-release")) -> dict[str, str]:
    """Parse the key/value subset used by os-release without executing it."""
    result: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, raw_value = line.split("=", 1)
        if not key.replace("_", "").isalnum():
            continue
        values = shlex.split(raw_value, posix=True)
        result[key] = values[0] if len(values) == 1 else raw_value
    return result


def filesystem_record(path: Path) -> dict[str, Any]:
    """Return byte-capacity information for the filesystem containing path."""
    usage = shutil.disk_usage(path)
    percent = 100.0 * usage.used / usage.total if usage.total else 0.0
    return {
        "path": str(path),
        "total_bytes": usage.total,
        "used_bytes": usage.used,
        "free_bytes": usage.free,
        "used_percent": round(percent, 2),
    }


def collect_inventory(paths: list[Path]) -> tuple[dict[str, Any], list[str]]:
    """Collect inventory and return it with nonfatal collection errors."""
    errors: list[str] = []
    try:
        os_release = parse_os_release()
    except (OSError, ValueError) as error:
        os_release = {}
        errors.append(f"os-release: {error}")

    filesystems: list[dict[str, Any]] = []
    for path in paths:
        try:
            filesystems.append(filesystem_record(path))
        except OSError as error:
            errors.append(f"filesystem {path}: {error}")

    data: dict[str, Any] = {
        "schema_version": 1,
        "collected_at": datetime.now(timezone.utc).isoformat(),
        "hostname": socket.getfqdn(),
        "kernel": platform.release(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "os": {
            "id": os_release.get("ID"),
            "version_id": os_release.get("VERSION_ID"),
            "pretty_name": os_release.get("PRETTY_NAME"),
        },
        "filesystems": sorted(filesystems, key=lambda item: item["path"]),
        "errors": errors,
    }
    return data, errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--path",
        action="append",
        dest="paths",
        metavar="PATH",
        help="filesystem path to report; repeatable (default: /)",
    )
    parser.add_argument("--pretty", action="store_true", help="indent JSON output")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    paths = [Path(value) for value in (args.paths or ["/"])]
    data, errors = collect_inventory(paths)
    json.dump(data, sys.stdout, indent=2 if args.pretty else None, sort_keys=True)
    sys.stdout.write("\n")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
