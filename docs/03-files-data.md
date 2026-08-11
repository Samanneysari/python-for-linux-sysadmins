# 03 — Files, Paths, JSON, CSV, Configuration, and Atomic Writes

## Outcome

Read and write Linux data without path confusion, partial files, encoding ambiguity, permission leaks, or unsafe deserialization.

## pathlib

```python
from pathlib import Path

config_path = Path("/etc/example-agent/config.json")
text = config_path.read_text(encoding="utf-8")
```

`Path` represents filesystem paths and composes them with `/`. A path object is not proof the target is safe. Symlinks, mount points, races, permissions, and namespaces matter.

## Text and bytes

```python
with path.open("r", encoding="utf-8", errors="strict") as handle:
    for line_number, line in enumerate(handle, start=1):
        process(line_number, line.rstrip("\n"))
```

Stream large files instead of `read_text`. Use strict decoding unless policy explicitly records replacement/loss. `rstrip()` without an argument removes meaningful spaces/tabs; remove only line endings when needed.

## JSON

```python
import json

data = json.loads(text)
if not isinstance(data, dict):
    raise ValueError("configuration root must be an object")
timeout = data.get("timeout_seconds", 5)
if not isinstance(timeout, int) or not 1 <= timeout <= 60:
    raise ValueError("timeout_seconds must be an integer from 1 to 60")
```

Parsing is not validation. JSON cannot represent comments and has no datetime/path type. Never trust a field simply because parsing succeeded.

## CSV

```python
import csv

with path.open("r", encoding="utf-8", newline="") as handle:
    for row in csv.DictReader(handle):
        process(row)
```

`newline=""` lets the CSV module manage newline conventions. CSV cells can become formulas when opened in spreadsheets; sanitize untrusted exported cells beginning with formula markers according to recipient policy.

## Configuration ownership

Do not treat Python source as configuration. Use a defined schema and separate secrets. Check owner/mode when policy requires, but remember ACLs and parent traversal:

```python
mode = config_path.stat().st_mode & 0o777
if mode & 0o077:
    raise PermissionError("configuration is accessible by group or others")
```

This is a policy example, not universal; group-readable service config can be correct. Symlink and race safety needs stronger file-opening design for hostile directories.

## Atomic replacement

Write a temporary file in the same filesystem/directory, flush it, set metadata, then replace:

```python
import os
import tempfile

parent = target.parent
with tempfile.NamedTemporaryFile(
    mode="w", encoding="utf-8", dir=parent, delete=False
) as handle:
    temp_path = Path(handle.name)
    json.dump(data, handle, indent=2, sort_keys=True)
    handle.write("\n")
    handle.flush()
    os.fsync(handle.fileno())

temp_path.chmod(0o600)
temp_path.replace(target)
```

Replacement is atomic on the same filesystem for the name transition, but complete durability may require syncing the directory and preserving owner/SELinux/ACL. A crash before replace leaves a temp file; clean safely.

## Unsafe formats

Do not load untrusted pickle; it can execute code during deserialization. YAML parsers and modes differ; if using a third-party YAML library, choose a safe loader and validate schema. Never use `eval` to parse data.

## Lab

Build an atomic JSON inventory writer with stable sorted output, mode policy, schema validation, a dry-run diff, and tests using `tempfile.TemporaryDirectory`.

## Review

1. Why is `Path.resolve()` not a complete authorization check?
2. Why stream large logs?
3. Why does successful JSON parsing not validate data?
4. What does same-filesystem replacement provide?
5. Why is untrusted pickle dangerous?
