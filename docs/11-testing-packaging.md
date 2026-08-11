# 11 — Testing, Packaging, and Reproducibility

## Outcome

Test decisions and side effects, build installable tools, isolate dependencies, and produce reproducible operational artifacts.

## Test pyramid for SysAdmin tools

- Unit: pure parsers, validators, classifiers, rendering.
- Component: subprocess wrapper with simulated outputs/errors/timeouts.
- Integration: disposable VM/container with real systemctl/network/filesystem.
- End-to-end: representative host and operational workflow including rollback.

Never run destructive tests on the developer workstation or production.

## unittest

```python
import unittest

class UsageTests(unittest.TestCase):
    def test_warning_boundary(self) -> None:
        self.assertEqual(classify_usage(85.0, warning=85.0), "warning")

    def test_rejects_impossible_percent(self) -> None:
        with self.assertRaises(ValueError):
            classify_usage(101.0)
```

Test boundaries, invalid input, missing files, permission failures, nonzero commands, timeout, malformed output, partial host failure, and stable JSON/exit codes.

## Temporary resources

Use `tempfile.TemporaryDirectory` and loopback/disposable services. Do not mock so much that command arguments, permissions, encoding, or Linux behavior are never tested.

## Mock subprocess at the boundary

Wrap command execution in one function or injectable runner. Assert exact argument list, `shell=False` default, timeout, environment, and error mapping.

## Packaging

`pyproject.toml` declares build system and project metadata. Build in a clean environment with approved tooling:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install build
python -m build
```

Third-party build dependencies must come from approved indexes/mirrors and reviewed versions. Test the wheel in a fresh environment. Do not upload internal tools to public PyPI accidentally; package names can be dependency-confusion targets.

## Dependencies

Minimize, pin/review according to policy, capture hashes/lock where tooling supports, scan licenses/vulnerabilities/provenance, and rebuild regularly. Vendoring creates its own update obligation. Standard library reduces but does not eliminate interpreter/platform risk.

## Compatibility

Test supported Python and distribution versions. Do not rely on internal/undocumented fields. Record minimum version from syntax and API use. `requires-python` communicates but does not test behavior.

## Review

1. What belongs in unit versus integration tests?
2. Why test failure paths?
3. Why use temporary directories?
4. What is dependency confusion?
5. Why test the built wheel in a fresh environment?
