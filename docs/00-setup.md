# 00 — Setup, Virtual Environments, and the First Tool

## Outcome

Install Python without damaging the OS package manager, create an isolated environment, and write a diagnostic program with a clear exit status.

## System Python versus application environment

Linux distributions use Python for system tools. Replacing packages in that interpreter can break package managers or utilities. Prefer:

- distribution package manager for OS-integrated libraries/tools;
- one `venv` per project/application;
- `pipx` or another approved mechanism for standalone Python CLIs;
- a built wheel installed into a dedicated service environment for production.

On RHEL family:

```bash
sudo dnf install python3 python3-pip
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip --version
```

On some distributions, the venv package is separate. `python3 -m venv .venv` creates an environment tied to that interpreter. Activation only adjusts the current shell; production services should call the absolute venv interpreter and never rely on activation.

Use module invocation:

```bash
python -m pip install --upgrade pip
```

This proves which interpreter owns pip. Review network/index policy before upgrades; production dependency changes require pinned/reviewed builds.

## First program

Create `hello_admin.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import platform
import socket

def main() -> int:
    hostname = socket.getfqdn()
    kernel = platform.release()
    print(f"host={hostname} kernel={kernel}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
```

Line by line:

- The shebang uses the caller's PATH; production systemd should use an absolute interpreter.
- Future annotations make type annotations less eager and ease forward references.
- Standard-library modules provide portable platform and socket helpers.
- `main` returns an integer contract.
- Local variables hold explicit values.
- The f-string formats one machine-readable-ish line; JSON is better for complex output.
- The module guard prevents automatic execution when imported by tests.
- `SystemExit` returns the chosen code to the shell.

Run and inspect:

```bash
python hello_admin.py
printf 'exit=%s\n' "$?"
python -m py_compile hello_admin.py
```

Compilation catches syntax errors, not logical/runtime/environment failures.

## Repository environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --editable .
python -m unittest discover -v
```

Editable installation exposes package entry points while source remains in place. It is convenient for development, not the immutable production deployment artifact.

## Lab

Print hostname, OS release, kernel, and current user as JSON. Return nonzero when `/etc/os-release` cannot be read. Write a unit test using a temporary path rather than editing the real file.

## Review

1. Why avoid `sudo pip install`?
2. What does activation change?
3. Why use a `main` return code?
4. What does compilation not test?
