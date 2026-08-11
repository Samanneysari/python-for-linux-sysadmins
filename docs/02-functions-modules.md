# 02 — Functions, Modules, Dataclasses, and Types

## Outcome

Separate pure decisions from Linux side effects and build reusable modules with explicit contracts.

## Small function

```python
def classify_usage(percent: float, warning: float = 85.0) -> str:
    if not 0.0 <= percent <= 100.0:
        raise ValueError("percent must be between 0 and 100")
    return "warning" if percent >= warning else "ok"
```

The function validates its domain, has no system side effect, returns one stable type, and can be unit-tested. Type hints help humans/tools; they do not automatically reject a string at runtime.

## Avoid mutable defaults

Wrong:

```python
def add_host(host: str, hosts: list[str] = []) -> list[str]:
    hosts.append(host)
    return hosts
```

The list is created once and shared across calls. Better:

```python
def add_host(host: str, hosts: list[str] | None = None) -> list[str]:
    result = [] if hosts is None else list(hosts)
    result.append(host)
    return result
```

## Dataclass

```python
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ServiceState:
    name: str
    active: bool
    substate: str
```

`frozen` prevents normal field reassignment and `slots` reduces accidental attributes/memory. It is not a security boundary and nested mutable fields can still mutate.

## Modules and packages

Put reusable code under `src/sysadmintools`, tests under `tests`, and tiny CLI orchestration in `main`. Importing a module should not start scans, modify files, or parse command-line arguments.

```python
def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return run(args)
```

Passing `argv` makes CLI tests deterministic.

## Dependency injection

Instead of hard-coding `subprocess.run` in every decision, pass a runner or split command execution from parsing:

```python
def parse_active_state(output: str) -> bool:
    fields = dict(line.split("=", 1) for line in output.splitlines() if "=" in line)
    return fields.get("ActiveState") == "active"
```

Pure parsing tests use fixed text; a smaller integration test exercises systemctl.

## Exceptions as contracts

Raise a specific exception when the caller can respond. Do not return a mixture of `None`, `False`, empty data, and strings for failures. Translate low-level errors at the boundary while preserving cause with `raise ... from error`.

## Lab

Build a module with frozen dataclasses for filesystem usage, a pure classifier, JSON conversion, and unit tests for 0, warning boundary, 100, and invalid values.

## Review

1. What makes a function pure?
2. Why are mutable defaults shared?
3. What do type hints not do?
4. Why avoid side effects at import time?
5. How does dependency injection help tests?
