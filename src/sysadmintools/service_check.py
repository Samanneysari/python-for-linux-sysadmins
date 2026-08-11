"""Query systemd unit state with bounded subprocess execution."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass


UNIT_PATTERN = re.compile(r"^[A-Za-z0-9_.@:-]+$")


@dataclass(frozen=True, slots=True)
class ServiceResult:
    unit: str
    load_state: str
    active_state: str
    sub_state: str
    result: str
    ok: bool
    error: str | None = None


def validate_unit(unit: str) -> str:
    if unit.startswith("-") or not UNIT_PATTERN.fullmatch(unit):
        raise ValueError(f"invalid unit name: {unit!r}")
    return unit


def parse_properties(output: str) -> dict[str, str]:
    properties: dict[str, str] = {}
    for line in output.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        properties[key] = value
    return properties


def check_service(unit: str, timeout: float = 10.0) -> ServiceResult:
    unit = validate_unit(unit)
    environment = {
        "PATH": "/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG": "C.UTF-8",
    }
    try:
        completed = subprocess.run(
            [
                "systemctl",
                "show",
                unit,
                "--property=LoadState,ActiveState,SubState,Result",
                "--no-pager",
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout,
            env=environment,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return ServiceResult(unit, "unknown", "unknown", "unknown", "unknown", False, str(error))

    properties = parse_properties(completed.stdout)
    load_state = properties.get("LoadState", "unknown")
    active_state = properties.get("ActiveState", "unknown")
    sub_state = properties.get("SubState", "unknown")
    result = properties.get("Result", "unknown")
    ok = completed.returncode == 0 and load_state == "loaded" and active_state == "active"
    error = None if completed.returncode == 0 else completed.stderr.strip() or f"exit {completed.returncode}"
    return ServiceResult(unit, load_state, active_state, sub_state, result, ok, error)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("units", nargs="+", help="systemd unit names")
    parser.add_argument("--timeout", type=float, default=10.0)
    parser.add_argument("--json", action="store_true", help="emit JSON")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if not 0.1 <= args.timeout <= 120.0:
        print("error: timeout must be from 0.1 to 120 seconds", file=sys.stderr)
        return 2
    try:
        results = [check_service(unit, args.timeout) for unit in args.units]
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps([asdict(result) for result in results], sort_keys=True))
    else:
        for result in results:
            print(
                f"{result.unit}: ok={str(result.ok).lower()} "
                f"load={result.load_state} active={result.active_state} "
                f"sub={result.sub_state} result={result.result}"
            )
    return 0 if all(result.ok for result in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
