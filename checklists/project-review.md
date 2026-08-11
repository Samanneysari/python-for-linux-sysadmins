# Python SysAdmin Tool Review

## Purpose and interface

- [ ] Problem, scope, users, supported Python/OS, and non-goals documented.
- [ ] Inputs validated by type/range/allowlist; configuration schema versioned.
- [ ] Human and JSON outputs have stable documented fields.
- [ ] stdout/stderr/logs and exit codes have explicit contracts.

## Safety and security

- [ ] Read-only default; changes require plan/apply and exact target validation.
- [ ] Idempotency, current-state check, rollback, and post-change validation tested.
- [ ] No shell-string construction; subprocess has argument list, timeout, return handling, bounded output, controlled environment.
- [ ] Filesystem paths constrained; symlink/race/broad deletion risks addressed.
- [ ] TLS verification enabled; URL/redirect/SSRF boundaries defined.
- [ ] Secrets excluded from source, arguments, logs, errors, tests, and fixtures.
- [ ] Least privilege; no unnecessary root or broad sudo rule.

## Reliability

- [ ] External calls have per-operation and total deadlines, bounded retries with jitter, and cancellation behavior.
- [ ] Concurrency, queues, cardinality, file/body/output sizes are bounded.
- [ ] Partial failure is represented, not silently ignored.
- [ ] Timezone-aware timestamps and monotonic durations used correctly.
- [ ] Atomic write/locking/crash behavior documented.

## Quality and deployment

- [ ] Pure decisions separated from side effects.
- [ ] Type hints/dataclasses and specific exceptions clarify contracts.
- [ ] Unit tests cover boundaries/errors; integration tests use disposable environment.
- [ ] `py_compile`, tests, package build, and clean-venv install pass.
- [ ] Dependencies/provenance/licenses/vulnerabilities reviewed.
- [ ] systemd unit uses absolute venv executable, dedicated user, sandbox, resource policy.
- [ ] Version, logs, metrics, runbook, rollback artifact, and owner exist.
