# 08 — Network, DNS, HTTP, and TLS Automation

## Outcome

Build bounded network checks that distinguish resolution, connection, TLS, HTTP, and application semantics.

## DNS through system APIs

```python
import socket

answers = socket.getaddrinfo(
    "app.example.net",
    443,
    type=socket.SOCK_STREAM,
)
```

`getaddrinfo` follows system resolver policy and may return IPv6/IPv4, duplicates, and ordered choices. It does not expose DNS TTL, authoritative chain, or raw records.

## TCP with timeout

```python
with socket.create_connection((host, port), timeout=3.0) as connection:
    peer = connection.getpeername()
```

This proves a TCP connection to one resolved address. It does not prove TLS, HTTP, authentication, or application health.

## HTTPS with standard library

```python
import ssl
import urllib.request

context = ssl.create_default_context()
request = urllib.request.Request(
    "https://app.example.net/health",
    headers={"User-Agent": "sysadmin-check/1.0"},
)
with urllib.request.urlopen(request, timeout=5, context=context) as response:
    body = response.read(4096)
```

The default context validates trust and hostname. Limit body size. `urlopen` follows redirects under handler policy; record final URL and restrict schemes/hosts for security-sensitive tools.

## SSRF in administration tools

A tool that fetches a user-supplied URL can reach loopback, cloud metadata, internal services, Unix gateways, or redirect there. Validate scheme, allowed host/domain, resolved addresses, redirects, ports, and DNS-rebinding risk. Network egress policy is defense in depth.

## API data

Set Accept/Content-Type, authentication through protected mechanisms, request ID, explicit timeout, response-size limit, status handling, JSON schema validation, retry budget, and pagination. Do not log bearer tokens or full sensitive responses.

## Concurrent checking

Use a bounded thread pool for several blocking HTTP checks. Keep per-request timeout and overall deadline; 1,000 threads are not a timeout strategy.

## Scenario: check says down, curl works

Compare resolver/address family, proxy environment, CA trust, SNI/hostname, redirect behavior, timeout, User-Agent/auth headers, IPv6, response-body requirement, and final URL. Emit each phase rather than one boolean.

## Review

1. What does `getaddrinfo` test and miss?
2. Why does TCP success not prove HTTPS?
3. Why keep certificate verification enabled?
4. How can a URL checker create SSRF?
5. Why limit response body and concurrency?
