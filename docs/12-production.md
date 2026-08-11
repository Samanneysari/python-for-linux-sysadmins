# 12 — Secure Production Automation

## Outcome

Deploy Python tools with least privilege, explicit configuration, secret safety, idempotency, locking, systemd lifecycle, observability, and rollback.

## Idempotency

An idempotent operation converges to desired state and reports whether it changed anything. Pattern:

1. inspect current state;
2. validate prerequisites and target;
3. plan exact difference;
4. apply one change;
5. validate desired and service-level state;
6. roll back on the defined failure boundary.

Avoid `check then act` races where another process changes state between steps. Use atomic APIs, locks, compare-and-swap/version checks, or tolerate conflict.

## Privilege separation

Run read-only logic unprivileged. For one protected action, use a narrow helper, systemd service/API, polkit, or sudo rule with fixed arguments and validated input. Review whether the privileged program can load config/plugins from writable paths.

## Secrets

Read secrets from an approved store or systemd credentials with narrow lifetime/permissions. Avoid environment and command arguments when exposure routes are unacceptable. Never log or include them in exception repr, process lists, support bundles, tests, or fixtures.

## Locking

Prevent overlapping jobs when harmful. systemd timer service activation already avoids simultaneous activation of the same unit under common behavior, but manual invocation or multiple hosts still race. File locks apply per filesystem/host and need defined stale/crash semantics.

## systemd service

```ini
[Unit]
Description=SysAdmin inventory collector
After=network.target

[Service]
Type=oneshot
User=inventory
Group=inventory
ExecStart=/opt/sysadmin-inventory/venv/bin/sysadmin-inventory --pretty
NoNewPrivileges=yes
PrivateTmp=yes
ProtectSystem=strict
ProtectHome=yes
ReadWritePaths=/var/lib/sysadmin-inventory
StateDirectory=sysadmin-inventory
```

- Absolute venv entry point avoids activation/PATH ambiguity.
- Dedicated identity and oneshot lifecycle fit a bounded collection.
- Sandboxing removes privilege and write access except managed state.
- Add network access controls/resource limits based on real requirements.

Timer:

```ini
[Timer]
OnCalendar=hourly
Persistent=yes
RandomizedDelaySec=10m
Unit=sysadmin-inventory.service

[Install]
WantedBy=timers.target
```

Persistent triggers a missed calendar run after activation; random delay spreads fleet load. The program must remain idempotent and bounded.

## Deployment

Build a wheel in trusted CI/build host, verify provenance/hash, install into versioned venv/artifact directory, point a stable symlink or unit to the reviewed version, validate, and keep previous artifact for rollback. Configuration/schema/data migrations need compatible rollback.

## Observability

Emit start/end, version, host, operation, target count, changed count, failures, duration, and stable exit code. Avoid high-cardinality secrets. Monitoring distinguishes never-ran, running-too-long, partial failure, stale output, and healthy.

## Review

1. What does idempotency require beyond no crash?
2. Why separate privilege?
3. What races remain across multiple hosts?
4. Why use an absolute venv entry point in systemd?
5. What should monitoring distinguish?
