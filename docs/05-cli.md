# 05 — Command-Line Interfaces with argparse

## Outcome

Build discoverable CLIs with typed validation, stable output, explicit dry-run/change modes, and useful exit codes.

## Parser

```python
import argparse

def percent(value: str) -> float:
    parsed = float(value)
    if not 0.0 <= parsed <= 100.0:
        raise argparse.ArgumentTypeError("must be between 0 and 100")
    return parsed

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Report filesystems above a usage threshold."
    )
    parser.add_argument("--threshold", type=percent, default=85.0)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--verbose", action="count", default=0)
    return parser
```

- Custom type rejects invalid data during parsing.
- Choices document and constrain output modes.
- Repeated verbosity flags can map to logging levels.

## Subcommands

Use `inspect`, `plan`, and `apply` subcommands for operational tools. Default to inspect/plan. An apply command should require exact target, current-state check, confirmation policy suitable for interactive/automation use, and post-change validation.

Interactive prompts are unsafe in unattended jobs and can be bypassed carelessly. Prefer an explicit `--apply`/subcommand plus change authorization outside the program. Never make `--yes` the only safety control.

## Output contract

- Human text goes to stdout on success.
- Errors/diagnostics go to stderr.
- JSON output has a documented schema and stable types.
- Logs should not corrupt machine-readable stdout; send to stderr or a separate handler.
- Exit code reflects overall contract; partial failures appear in output and documented code.

```python
print(json.dumps(result, sort_keys=True))
print(f"error: {error}", file=sys.stderr)
```

## Destructive target validation

For a cleanup tool, allow only descendants of configured roots, reject root/home/workspace broad paths, resolve symlinks carefully, refuse empty/unresolved variables, list the plan, and re-check immediately before action. Race-resistant filesystem operations may require directory file descriptors and platform-specific APIs.

## Testing parser

```python
args = build_parser().parse_args(["--threshold", "90", "--format", "json"])
assert args.threshold == 90.0
```

Test invalid values expecting `SystemExit(2)` without launching a subprocess.

## Review

1. Why validate in argparse types?
2. Why separate machine stdout from logs?
3. Why is a confirmation prompt insufficient safety?
4. What should dry-run contain?
5. Why pass `argv` into `main`?
