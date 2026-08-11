# 09 — Logs, Regular Expressions, and Time

## Outcome

Stream large logs, parse structured data first, use regex carefully, normalize timestamps, and summarize without losing important errors.

## Prefer structured logs

JSON Lines gives one JSON object per line:

```python
import json

for line_number, line in enumerate(handle, start=1):
    try:
        event = json.loads(line)
    except json.JSONDecodeError as error:
        logger.warning("invalid JSON line=%d error=%s", line_number, error)
        continue
```

Define policy for malformed records: fail, skip with count, quarantine, or partial result. Silent skipping corrupts conclusions.

## Regex

```python
import re

FAILED_SSH = re.compile(
    r"Failed password for (?:invalid user )?(?P<user>\S+) from (?P<ip>\S+)"
)
```

- Raw strings reduce Python escaping confusion.
- Named groups make meaning explicit.
- `\S+` remains a heuristic, not IP validation.
- Log formats vary by version/locale/config and attacker-controlled fields can manipulate matches.

Use `ipaddress.ip_address` to validate an address. Avoid catastrophic backtracking on untrusted large input; bound line length and prefer simple patterns.

## Time

```python
from datetime import datetime, timezone

now = datetime.now(timezone.utc)
rendered = now.isoformat()
```

Use timezone-aware datetimes. Preserve raw timestamp and zone, then derive UTC. DST creates ambiguous/nonexistent local times. `time.monotonic()` is for durations/deadlines because wall clock can jump.

```python
import time

start = time.monotonic()
run_check()
elapsed = time.monotonic() - start
```

## Rotation and following

Following a filename must handle rename/recreate, truncation, inode change, and permissions. For production ingestion prefer journald/syslog/filebeat-like supported mechanisms rather than a home-grown endless tailer. A batch parser should record file inode/hash/offset and whether input changed during processing.

## Memory-safe summaries

Use `collections.Counter`, heaps, and streaming aggregations instead of storing every event. Enforce maximum unique keys to prevent untrusted high-cardinality data from exhausting memory.

## Journal JSON

`journalctl -o json --no-pager` provides structured fields. Invoke with argument list/timeout and parse line by line. Binary/non-UTF fields may be encoded or absent; journal selection and privileges affect completeness.

## Review

1. Why is malformed-record policy important?
2. Why validate regex-captured IPs?
3. Why use monotonic time for durations?
4. What breaks a naive log follower?
5. How can high cardinality exhaust memory?
