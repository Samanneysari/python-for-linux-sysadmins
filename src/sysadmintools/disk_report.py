"""Report byte usage for selected filesystem paths."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class DiskResult:
    path: str
    total_bytes: int | None
    used_bytes: int | None
    free_bytes: int | None
    used_percent: float | None
    status: str
    error: str | None = None


def classify(percent: float, warning: float, critical: float) -> str:
    if not 0.0 <= percent <= 100.0:
        raise ValueError("percent must be between 0 and 100")
    if not 0.0 <= warning < critical <= 100.0:
        raise ValueError("thresholds must satisfy 0 <= warning < critical <= 100")
    if percent >= critical:
        return "critical"
    if percent >= warning:
        return "warning"
    return "ok"


def check_path(path: Path, warning: float, critical: float) -> DiskResult:
    try:
        usage = shutil.disk_usage(path)
    except OSError as error:
        return DiskResult(str(path), None, None, None, None, "unknown", str(error))
    percent = 100.0 * usage.used / usage.total if usage.total else 0.0
    return DiskResult(
        str(path),
        usage.total,
        usage.used,
        usage.free,
        round(percent, 2),
        classify(percent, warning, critical),
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", metavar="PATH")
    parser.add_argument("--warning", type=float, default=85.0)
    parser.add_argument("--critical", type=float, default=95.0)
    parser.add_argument("--json", action="store_true")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        classify(0.0, args.warning, args.critical)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    results = [check_path(Path(value), args.warning, args.critical) for value in args.paths]
    if args.json:
        print(json.dumps([asdict(result) for result in results], sort_keys=True))
    else:
        for result in results:
            percent = "unknown" if result.used_percent is None else f"{result.used_percent:.2f}%"
            print(f"{result.path}: status={result.status} used={percent}")
    statuses = {result.status for result in results}
    if "unknown" in statuses or "critical" in statuses:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
