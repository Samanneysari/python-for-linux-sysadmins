# Automation Safety

## Before a program changes Linux

- Identify exact host, user, namespace/container, path, service, and environment.
- Validate input type, allowed values, canonical target, and current state.
- Default to read-only and support `--dry-run` for changes.
- Make one idempotent change and verify the desired result.
- Define rollback and preserve metadata/content securely.
- Use least privilege for the smallest operation.
- Set timeouts and bounded concurrency for every external dependency.
- Log decisions and outcomes without secrets.

## Never

- build a shell command by concatenating untrusted strings;
- use `shell=True` unless shell semantics are required and every input is fixed/trusted;
- deserialize untrusted pickle data;
- disable TLS verification to make an API pass;
- store passwords/tokens in source, command arguments, or logs;
- recursively delete a path without resolving and validating an allowed root;
- catch every exception and pretend success;
- run the entire tool as root because one subcommand needs privilege;
- edit the distribution-managed Python environment with `sudo pip`.

## Exit-code contract

- `0`: requested operation completed and validation passed.
- `1`: operational failure.
- `2`: invalid command-line usage (the common argparse convention).
- Other codes may represent stable documented categories; do not invent different meanings per run.

Scripts used by monitoring must distinguish unknown/tool failure from healthy state.
