# Python for Linux System Administrators

A practical, beginner-friendly path from Python fundamentals to safe Linux administration tools.

The goal is not to replace shell scripts with Python blindly. The goal is to know when Python gives clearer data structures, validation, testing, error handling, concurrency, and maintainability—and to integrate it with Linux without unsafe shell construction.

Examples target maintained Python 3 versions and use the standard library first. Check the Python version shipped and supported by your distribution.

## Curriculum

| Chapter | Outcome |
| --- | --- |
| [00 — Setup and first tool](docs/00-setup.md) | Install safely, use `venv`, and write a first diagnostic CLI. |
| [01 — Language fundamentals](docs/01-fundamentals.md) | Understand objects, values, collections, conditions, loops, and comprehensions. |
| [02 — Functions, modules, and types](docs/02-functions-modules.md) | Build reusable, typed, testable modules. |
| [03 — Files and structured data](docs/03-files-data.md) | Use pathlib, text, JSON, CSV, config, permissions, and atomic writes. |
| [04 — Exceptions and logging](docs/04-errors-logging.md) | Fail clearly, preserve causes, emit useful structured operational logs. |
| [05 — Command-line interfaces](docs/05-cli.md) | Build trustworthy `argparse` tools with exit codes and dry runs. |
| [06 — subprocess and Linux commands](docs/06-subprocess.md) | Execute commands without injection, hangs, or hidden failure. |
| [07 — Linux system data](docs/07-linux-data.md) | Inspect processes, services, filesystems, users, `/proc`, and systemd. |
| [08 — Network and HTTP automation](docs/08-network.md) | Resolve names, connect with timeouts, validate TLS, and call APIs. |
| [09 — Logs, regex, and time](docs/09-logs-time.md) | Parse streams, normalize time, summarize events, and handle rotation. |
| [10 — Concurrency](docs/10-concurrency.md) | Use threads, processes, and asyncio only where they fit. |
| [11 — Testing and packaging](docs/11-testing-packaging.md) | Test behavior, isolate side effects, package internal tools, and pin intentionally. |
| [12 — Secure production automation](docs/12-production.md) | Handle privilege, secrets, config, idempotency, locking, systemd, and rollback. |
| [13 — Capstone projects](docs/13-projects.md) | Combine skills into production-shaped SysAdmin tools. |

Practice:

- [40 labs](labs/README.md)
- [100 exercises](exercises/questions.md) and [answer key](exercises/answers.md)
- Tested examples under [`src/sysadmintools`](src/sysadmintools)
- Unit tests under [`tests`](tests)
- [Project review checklist](checklists/project-review.md)
- [Official references](REFERENCES.md)

## Supported learning environment

Use a normal account on a disposable Rocky/AlmaLinux or Ubuntu VM. Most examples require no root. When data requires privilege, the guide explains why; do not run the entire program as root merely for convenience.

## Conventions

- Code is English and formatted for readability.
- `<value>` means replace the placeholder.
- Examples avoid third-party dependencies unless a chapter explicitly explains them.
- All external commands use argument lists, timeouts, captured results, and checked return codes.
- Destructive actions must support plan/dry-run, explicit target validation, and post-change verification.

This repository complements the Bash and Linux guides. Bash remains excellent for small command pipelines; Python becomes valuable when state, parsing, validation, APIs, testing, and maintenance grow.
