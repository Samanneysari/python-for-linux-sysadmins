# 07 — Linux System Data

## Outcome

Gather users, processes, services, filesystems, and `/proc` data using the correct interface and explicit limitations.

## Prefer stable APIs where available

- `platform`, `os`, `pwd`, `grp`, `shutil`, `resource`, `socket` for local information.
- `/proc` and `/sys` for Linux-specific runtime state with kernel documentation.
- D-Bus/systemd APIs for robust applications; `systemctl show` is a practical CLI boundary.
- Structured command output such as `ip -json`.

## Users and groups

```python
import pwd

for entry in pwd.getpwall():
    print(entry.pw_name, entry.pw_uid, entry.pw_dir, entry.pw_shell)
```

`pwd` reads local account database semantics and may not represent every central identity query. `getent` follows NSS and is often better for enterprise identity inventory.

## Filesystem usage

```python
from pathlib import Path
from shutil import disk_usage

usage = disk_usage(Path("/var"))
percent = 100.0 * usage.used / usage.total if usage.total else 0.0
```

This returns byte capacity for the filesystem containing the path; it does not report inode usage, quotas, thin-pool state, read-only mounts, or deleted-open files.

## `/proc`

Read one process safely:

```python
status_path = Path(f"/proc/{pid}/status")
try:
    status = status_path.read_text(encoding="utf-8")
except FileNotFoundError:
    return None
```

Processes exit between listing and reading; this is normal. Validate PID integer/range. `/proc` text formats are documented but Linux-specific. Permissions and hidepid settings limit visibility.

## systemd state

Call:

```bash
systemctl show nginx.service --property=LoadState,ActiveState,SubState,Result --no-pager
```

Parse `KEY=value` lines and preserve unknown/missing fields. `active` does not prove an application transaction.

## OS release

Parse `/etc/os-release` according to its format; do not execute/source it in Python. Quoting and escapes need a proper parser or narrowly tested implementation.

## Inventory boundaries

Inventory should declare whether it covers host or container namespace, local versus central users, current versus persistent firewall, mounted versus all block devices, and unprivileged versus root-visible processes.

## Review

1. Why can `pwd` differ from `getent`?
2. What does `disk_usage` miss?
3. Why can `/proc/<PID>` disappear?
4. Why is `ActiveState=active` insufficient health?
5. Why should `/etc/os-release` not be sourced as arbitrary shell?
