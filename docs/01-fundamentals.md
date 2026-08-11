# 01 — Language Fundamentals

## Outcome

Use Python values and control flow predictably while avoiding mutable-state and truthiness mistakes.

## Names and objects

```python
threshold = 90
filesystem = "/var"
message = f"{filesystem} threshold is {threshold}%"
```

Names reference objects; assignment does not declare a fixed type. Type annotations and tests communicate expectations but Python normally enforces behavior at runtime.

## Core values

- `None`: absence/no value; compare with `is None`.
- `bool`: `True`/`False`.
- `int` and `float`: integer and binary floating point. Use `decimal.Decimal` for exact decimal policy when required.
- `str`: Unicode text.
- `bytes`: raw bytes; decode with an explicit encoding/error policy.

```python
raw = b"node01\n"
name = raw.decode("utf-8").strip()
```

Do not silently discard decode errors in logs without recording loss.

## Collections

```python
ports = [22, 80, 443]
unique_hosts = {"web1", "web2"}
service = {"name": "nginx", "active": True, "ports": ports}
identity = ("web1", "192.0.2.10")
```

- list: ordered mutable sequence.
- set: unique hashable values; unordered for semantic purposes.
- dict: key/value mapping with insertion order preserved, but do not confuse order with sorted data.
- tuple: immutable sequence.

## Mutation and copying

```python
original = {"checks": ["disk", "dns"]}
shallow = original.copy()
shallow["checks"].append("tls")
```

Both mappings still reference the same nested list. Use `copy.deepcopy` only when its semantics fit; often constructing explicit new data is clearer.

## Conditions

```python
if usage_percent >= 95:
    severity = "critical"
elif usage_percent >= 85:
    severity = "warning"
else:
    severity = "ok"
```

Validate units/ranges first. `0`, empty collections/strings, `None`, and `False` are falsey but mean different things operationally. Do not write `if value` when zero is valid and `None` means unknown.

## Loops

```python
for index, mount in enumerate(mounts, start=1):
    print(index, mount)

for host, address in sorted(hosts.items()):
    print(host, address)
```

Sort when stable output matters for diffs/tests. Do not modify a dict/set while iterating it; iterate over a copy or construct a new result.

## Comprehensions

```python
critical = [item for item in filesystems if item["percent"] >= 95]
by_mount = {item["mount"]: item for item in filesystems}
```

Use comprehensions for one clear transformation/filter. Multi-level side effects belong in normal loops/functions.

## Equality and identity

Use `==` for value equality and `is` for singleton identity such as `None`. String interning can make `is` appear to work until it does not.

## Lab

Given filesystem dictionaries, validate required keys/ranges, sort by percentage descending, classify severity, and output a new list without modifying input.

## Review

1. How do `str` and `bytes` differ?
2. Why can a shallow copy surprise you?
3. Why distinguish zero from `None`?
4. When should output be sorted?
