# 06 — subprocess and Linux Command Integration

## Outcome

Execute Linux commands with exact arguments, timeouts, return-code handling, bounded output, and no shell injection.

## Safe baseline

```python
import subprocess

completed = subprocess.run(
    ["systemctl", "show", "nginx.service", "--property=ActiveState"],
    check=True,
    capture_output=True,
    text=True,
    timeout=10,
)
output = completed.stdout
```

- Argument list bypasses shell parsing.
- `check=True` raises `CalledProcessError` on nonzero status.
- Capture separates stdout/stderr; large/unbounded output can consume memory.
- Text mode decodes using locale unless encoding is specified.
- Timeout bounds waiting and raises `TimeoutExpired`.

## Never concatenate shell input

Unsafe:

```python
subprocess.run(f"journalctl -u {unit}", shell=True)
```

An attacker-controlled unit can inject shell syntax. Safer:

```python
subprocess.run(["journalctl", "-u", unit, "--no-pager"], check=True)
```

Still validate `unit` against the tool's allowed domain to prevent surprising options or excessive access. Use `--` where the called program supports it.

## Environment

```python
import os

environment = {
    "PATH": "/usr/sbin:/usr/bin:/sbin:/bin",
    "LANG": "C.UTF-8",
}
subprocess.run(["ip", "-json", "address"], env=environment, check=True)
```

Do not inherit attacker-controlled PATH, Python variables, proxies, or locale blindly in privileged execution. A minimal environment can break legitimate commands; define/test it.

## Parse structured output

Prefer `ip -json`, `systemctl show`, JSON APIs, or documented machine formats. Human tables change by locale/version and wrap unpredictably.

## Streaming and deadlocks

For long commands, iterate stdout with `Popen`, merge/consume stderr deliberately, enforce deadline, and terminate the process group safely. A child can spawn descendants; killing only one PID may not end the job. Use systemd transient units for complex resource/lifecycle control.

## Privilege

Do not call arbitrary `sudo` inside unattended code. Grant a narrow helper/polkit/sudo rule or run a small systemd service with explicit API and validation. Command-line arguments may appear in process listings.

## Error translation

Report executable missing, timeout, signal, exit code, and sanitized stderr separately. Do not turn all into `command failed` or silently parse partial stdout.

## Review

1. What does `check=True` change?
2. Why is `shell=True` risky?
3. Why prefer structured command output?
4. What risks exist in inherited environment?
5. Why can timeout handling leave descendants?
