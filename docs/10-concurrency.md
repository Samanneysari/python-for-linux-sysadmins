# 10 — Concurrency without Chaos

## Outcome

Choose sequential, threads, processes, or asyncio from workload and operational requirements, then bound cancellation, ordering, and resource use.

## Start sequential

Sequential code is easiest to reason about and often fast enough for tens of hosts. Measure before concurrency. Concurrency adds partial failure, ordering, races, cancellation, shared-state, rate-limit, and shutdown complexity.

## Thread pool for blocking I/O

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

with ThreadPoolExecutor(max_workers=8) as executor:
    futures = {executor.submit(check_host, host): host for host in hosts}
    for future in as_completed(futures):
        host = futures[future]
        try:
            results[host] = future.result()
        except Exception as error:
            failures[host] = str(error)
```

Eight is an explicit bound, not a universal optimum. Each operation also needs a timeout. `with` waits for submitted work on exit; design overall deadlines/cancellation if that is too long.

## Processes for CPU work

Process pools bypass the normal CPython GIL for CPU-heavy work but require picklable tasks/data, consume memory, and complicate logs/startup. Hashing may already execute optimized C and storage can be the bottleneck; measure.

## asyncio

Asyncio fits many concurrent sockets when libraries are async. It does not make blocking `subprocess.run`, file I/O, or synchronous HTTP automatically nonblocking. One blocking call stalls the event loop.

```python
async def check(host: str) -> Result:
    async with asyncio.timeout(5):
        reader, writer = await asyncio.open_connection(host, 443)
        writer.close()
        await writer.wait_closed()
        return Result(host=host, ok=True)
```

This only checks TCP and omits TLS/application semantics; it is a lifecycle example.

## Shared state and ordering

Collect each task result independently, then sort for stable output. Avoid many workers mutating one file/dict. Use queues, locks, or single-writer design where needed. Locks protect invariants, not distributed hosts; file locks have filesystem/process semantics and stale/remote considerations.

## Backpressure

Bound input queue, workers, per-target rate, retries, output size, and total deadline. Respect API rate limits. A monitoring tool that overwhelms the service creates its own incident.

## Review

1. Why start sequential?
2. What workload fits threads?
3. What costs accompany processes?
4. Why can blocking code freeze asyncio?
5. How does a single-writer design help?
