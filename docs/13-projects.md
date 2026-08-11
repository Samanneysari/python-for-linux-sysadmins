# 13 — Capstone Projects

## Project 1 — Inventory collector

Collect OS, kernel, hostname, Python, filesystem, and selected service state as stable JSON. Requirements: no root, explicit schema/version, bounded subprocess, partial-failure representation, deterministic output, tests, systemd timer, atomic result file.

## Project 2 — Service health checker

Accept validated unit names, query `systemctl show`, optionally run a separate application check, distinguish inactive/failed/not-found/tool-error, output text/JSON, support many hosts with bounded concurrency, and never equate active with healthy.

## Project 3 — Disk and inode alert

Read mount data, bytes and inode capacity, excludes pseudo filesystems, handles vanished mounts, compares warning/critical thresholds, and sends result through a pluggable reporter. Include deleted-open-file diagnostic hint without requiring root.

## Project 4 — Log summarizer

Stream journal JSON or JSON Lines, validate timestamps/fields, count error categories, cap cardinality, preserve malformed count, output top-N and time window, never log sensitive payload, and test rotation/truncated input.

## Project 5 — HTTPS fleet checker

Resolve, connect, validate TLS hostname/chain, issue bounded HTTP request, inspect status/content/timing/certificate expiry, restrict URLs to an allowlist, avoid SSRF/redirect escape, and check many endpoints with a small pool.

## Project 6 — Backup verifier

Verify manifest hashes, expected object count/size/date, immutable destination policy signal, and one isolated restore/application test record. It must not call a successful copy job a successful backup.

## Project 7 — Safe configuration deployer

Inspect/plan/apply one known config type. Validate schema and current version, atomically write with metadata/SELinux plan, run native validator, reload exact service, run remote check, and restore previous file on failure. Use disposable lab only.

## Project 8 — Incident evidence organizer

Create case/evidence IDs, copy authorized exports, record hashes/tool/source/time/custody, verify transfers, produce a timeline CSV, and enforce permissions. It must never execute collected artifacts.

## Graduation capstone

Combine inventory, service check, disk status, HTTPS validation, JSON logs, tests, package, systemd timer, atomic state, and monitoring contract. Seed timeout, malformed command output, DNS failure, permission denial, partial host failure, disk threshold, and stale result. Score safety and explainability above code length.

## Definition of done

- Clear threat/failure model and scope.
- No unsafe shell construction or embedded secrets.
- Typed internal data and validated external data.
- Timeouts, bounded resources, stable exit/output contract.
- Dry-run/idempotency/rollback for changes.
- Unit plus disposable integration tests.
- Least-privilege systemd deployment.
- Logs/metrics/runbook and operator-friendly errors.
- Fresh-environment installation and rollback demonstrated.
