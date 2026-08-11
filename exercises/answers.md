# Answer Key

1. A short, clear command pipeline with simple error behavior and no complex state/parsing is often better in Bash.
2. It can replace files/dependencies required by OS tools and conflict with package ownership or externally-managed policy.
3. It isolates interpreter entry points and site packages while sharing the base interpreter/standard library implementation.
4. It binds pip to the selected interpreter rather than whichever `pip` executable PATH finds.
5. It prepends environment binaries and sets shell variables; it does not change systemd or other processes.
6. Services do not run an activated interactive shell; absolute paths make version and environment explicit.
7. It prevents CLI execution when the module is imported for tests or reuse.
8. It creates a testable stable shell/monitoring contract via `SystemExit`.
9. Syntax/import-bytecode compilation succeeds; it does not prove logic, dependencies, permissions, or Linux behavior.
10. Editable install points into changing source for development; production should use a reviewed immutable build artifact.
11. `str` is Unicode text; `bytes` is raw octets requiring explicit encoding/decoding.
12. Locale defaults vary and silent replacement can corrupt evidence or configuration.
13. List is ordered mutable sequence; set unique values; dict key/value mapping; tuple immutable sequence.
14. The outer mapping is copied but both reference the same nested list/object.
15. They represent absent, numeric zero, present-but-empty text, and boolean false; truthiness alone loses meaning.
16. `==` compares values; `is` compares object identity and is appropriate for `None`.
17. Stable ordering improves diffs, tests, reproducibility, and incident comparison.
18. When logic has multiple conditions/levels, side effects, error handling, or needs readable intermediate names.
19. Structural mutation can invalidate iteration or skip/duplicate behavior; build a new mapping or iterate a snapshot.
20. Exact decimal financial/policy calculations where binary floating approximation is unacceptable.
21. Same inputs produce same output without external state mutation/observation.
22. It protects the function contract at every caller and produces early specific errors.
23. Defaults are evaluated once at function definition, so one object is reused.
24. Normally nothing automatically; static checkers/IDEs and humans use them unless runtime validation is added.
25. Nested mutable members, external resources, and security; normal field assignment is only restricted.
26. Import should be safe/reusable; scans, argument parsing, network, or writes make tests and composition unpredictable.
27. Tests can call the CLI parser directly without mutating global `sys.argv` or spawning a process.
28. Pure parser tests are deterministic and side-effect execution is isolated for integration/mocking.
29. Supplying a dependency/runner/config from outside instead of hard-coding it, enabling substitution and testing.
30. It retains low-level traceback/context while adding domain-specific meaning.
31. It offers readable path composition and file APIs with explicit path objects.
32. Authorization must handle allowed roots, symlinks, mounts, permissions, namespaces, and races immediately at operation.
33. It bounds memory and permits progressive processing/error reporting.
34. It removes all trailing whitespace, which may be meaningful; remove only known newline characters.
35. Syntax/types at the JSON grammar level can succeed while required fields, domain types/ranges, and relationships are wrong.
36. It lets the CSV module correctly handle platform newline conventions and quoted embedded newlines.
37. Spreadsheet applications may interpret cells beginning with special markers as formulas/commands when opened.
38. ACLs, parent traversal, ownership, SELinux/AppArmor, capabilities, mount policy, and namespace also affect access.
39. It atomically changes the directory name entry on the same filesystem; durability, metadata/labels, locking, and crash cleanup need more work.
40. Loading can execute attacker-controlled code by design.
41. When adding actionable context, translating to a stable boundary, retrying safely, or guaranteeing cleanup.
42. Broad catches hide bugs and may intercept conditions the program cannot recover from.
43. Its exit method runs on normal or exceptional exit, enabling deterministic resource cleanup.
44. The application owns global handlers/levels/format/destination; library configuration surprises consumers.
45. Passwords, tokens, private keys, cookies, full environment/commands, personal or regulated data, sensitive bodies.
46. Untrusted newlines/control characters can create fake entries or manipulate terminals/collectors.
47. Transient network/service/rate failures when operation is idempotent and retry budget exists—not auth/input/config failures.
48. It spreads clients so they do not retry simultaneously and recreate overload.
49. Retain per-target successes/failures, report partial status clearly, and return a documented nonzero result when contract is incomplete.
50. Normal users need concise safe errors; controlled debug preserves traceback without always exposing internals/secrets.
51. It gives early help/usage errors and typed constrained inputs before side effects.
52. Machine pipelines consume stdout; diagnostics/errors belong on stderr so schemas remain valid.
53. Stable schema version, typed fields, units, timestamps/zones, per-target status/errors, and no logs/secrets.
54. It does not validate target/current state, constrain scope, provide rollback, or prevent automation mistakes.
55. Exact resolved targets, current state, proposed differences, prerequisites, validation, and rollback—while making no mutation.
56. Target can change between resolution/check and use; use trusted directories, descriptor-relative/atomic operations, and immediate revalidation.
57. Callers and monitoring need stable meanings for healthy, operational failure, and usage error.
58. They may be parsed by a downstream command as flags even in an argument list; validate domain and use `--` where supported.
59. It raises `CalledProcessError` for nonzero exit; timeout and missing executable still use other exceptions.
60. It bypasses shell tokenization/metacharacter expansion and preserves exact argument boundaries.
61. Only when shell language is the fixed intended program and every dynamic input is eliminated or safely handled; prefer a reviewed script.
62. External commands can hang on locks, network, prompts, devices, or bugs and block automation indefinitely.
63. Output can be huge/sensitive and consume memory; stream or bound it when needed.
64. PATH/proxy/Python/locale variables can select wrong executables, leak secrets, change parsing, or inject behavior.
65. Human tables change by locale/version/wrapping; structured output has defined fields/types.
66. Executable/argv (sanitized), timeout versus signal versus exit code, bounded stderr, target/context, and cause.
67. It may spawn descendants or a process group/session; terminating one PID leaves work running.
68. Privilege boundary becomes broad and input-driven; use a narrow reviewed helper/polkit/sudo/systemd API.
69. `pwd` exposes local database APIs; `getent` follows configured NSS and can include central identities.
70. Inodes, quota, read-only state, deleted-open files, thin pools, separate submounts, latency/errors.
71. The process can exit or PID can be reused between enumeration and read; handle races as normal.
72. It may not listen, dependencies may fail, readiness may be false, or user transaction may be broken.
73. Sourcing executes shell content; parsing treats it as data and can validate supported format.
74. Host/container namespace, privilege visibility, local/central users, runtime/persistent policy, mounted/all storage, and time.
75. System resolver/NSS address selection for a socket type; it misses raw DNS TTL/records/delegation.
76. TLS protocol, SNI/name/trust/clock, HTTP, authentication, and application can fail after transport.
77. It uses maintained secure defaults and system trust/hostname verification instead of disabling identity checks.
78. User URLs/redirects/DNS can target loopback, metadata, internal networks, alternate ports, or rebinding addresses.
79. Redirect can escape the allowlist and unbounded bodies consume memory or expose data.
80. Status, content type, body limit, JSON schema/types, pagination, auth, rate limits, retries, timeouts, and final endpoint.
81. Fields/types avoid fragile text matching; regex remains useful for legacy unstructured lines.
82. Catastrophic backtracking can consume CPU; input can be huge/attacker-controlled and format changes create false matches.
83. A captured token only looks like an IP; `ipaddress` enforces syntax/domain.
84. It avoids ambiguous local time and permits correct cross-host ordering/conversion.
85. Wall clock can jump due to synchronization/manual changes; monotonic only moves forward for intervals.
86. Rename/recreate, truncate, inode change, permissions, partial line, rotation/compression, restart offset, and deletion.
87. Millions of unique attacker-controlled keys grow dict/set memory; cap and aggregate.
88. It is simpler, deterministic, often sufficient, and establishes a performance baseline before complexity.
89. Many independent blocking network/subprocess operations with bounded workers and timeouts.
90. CPU-heavy independent work with picklable inputs where memory/startup/IPC cost is justified.
91. Synchronous calls occupy the event-loop thread and prevent other tasks from progressing.
92. Bounded acceptance/queues/concurrency/rate that prevents producers from overwhelming consumers.
93. Completion order varies; sorting makes output/tests/diffs stable without changing execution concurrency.
94. Unit tests pure decisions; integration tests real Linux boundaries in disposable systems; end-to-end tests full operational workflow/rollback.
95. Production mostly experiences permissions, missing data, timeouts, malformed output, partial hosts, and cleanup failures—not only happy paths.
96. A public package can be named like an internal dependency and be selected by an index resolver if source policy is weak.
97. Inspect current state, compute difference, converge safely, report changed/unchanged, validate result, and tolerate repeated execution.
98. It limits compromise and mistakes; grant only the protected action through a narrow interface rather than run all parsing/network logic as root.
99. Never ran, currently running, exceeded deadline, failed/partial, produced stale result, and healthy with last-success time/version.
100. Safe validated inputs, inventory/disk/service/HTTPS semantics, bounded failure/concurrency, stable JSON/exit/logs, tests, package/fresh install, least-privilege systemd/timer, rollback and seeded-failure success.
