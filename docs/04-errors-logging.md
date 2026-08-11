# 04 — Exceptions and Operational Logging

## Outcome

Make failures explicit, preserve causes, clean resources, and emit logs that operators can act on without leaking secrets.

## Exception boundaries

Catch exceptions where you can add context, retry safely, translate to a stable CLI/API result, or clean resources. Do not wrap an entire program in `except Exception: pass`.

```python
try:
    config = load_config(path)
except FileNotFoundError as error:
    raise ConfigError(f"configuration not found: {path}") from error
except PermissionError as error:
    raise ConfigError(f"configuration not readable: {path}") from error
```

`raise ... from error` keeps the causal chain. User-facing CLI output can be concise while debug logs retain traceback under controlled access.

## Cleanup with context managers

```python
with path.open("rb") as handle:
    digest = hash_stream(handle)
```

The file closes even when hashing raises. Use context managers for files, locks, temporary directories, sockets, and transactions.

## Do not catch process exits blindly

`KeyboardInterrupt`, `SystemExit`, and some fatal conditions do not belong in ordinary recovery. Catch specific exceptions. If a loop handles per-host failure, record it and continue only when partial success is part of the contract.

## Logging

```python
import logging

logger = logging.getLogger(__name__)

def check_host(host: str) -> None:
    logger.info("starting host check", extra={"host": host})
```

Libraries should not call `basicConfig`; the CLI/application owns handlers, format, destination, and level.

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
```

Use UTC consistently when correlating hosts; configure a formatter/converter or emit structured timestamps deliberately.

## Secrets and log injection

Never log passwords, bearer tokens, private keys, cookies, full environment, or sensitive command output. Untrusted values can include newlines/control characters and forge text logs. Structured logging plus escaping/sanitization helps, but access/retention still matter.

## Retry

Retry only transient operations, with bounded attempts, deadline, exponential backoff plus jitter, and idempotent behavior. Do not retry authentication failure, invalid input, or deterministic config errors.

## CLI boundary

```python
def main() -> int:
    try:
        run()
    except ConfigError as error:
        logger.error("configuration error: %s", error)
        return 2
    except OperationalError as error:
        logger.error("operation failed: %s", error)
        return 1
    return 0
```

Do not expose stack traces to normal users by default; provide a controlled debug mode.

## Review

1. When should an exception be caught?
2. Why preserve cause?
3. Why should libraries not configure global logging?
4. Which failures should not be retried?
5. How can untrusted values forge text logs?
