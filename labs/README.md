# Python SysAdmin Labs

| ID | Lab | Required behavior |
| --- | --- | --- |
| P01 | venv and interpreter proof | Show exact Python/pip paths and versions |
| P02 | First JSON inventory | Stable schema and exit code |
| P03 | Values and validation | Distinguish zero, empty, false, unknown |
| P04 | Collection copy behavior | Avoid unintended nested mutation |
| P05 | Filesystem severity | Test boundaries and invalid percentages |
| P06 | Dataclass service state | Frozen typed result |
| P07 | Module without import side effect | Tests can import safely |
| P08 | Dependency-injected parser | Test without real systemctl |
| P09 | Stream a large text file | Bounded memory and malformed lines |
| P10 | JSON schema validation | Reject wrong root/types/ranges |
| P11 | CSV read/write | Correct newline and formula-risk policy |
| P12 | Atomic JSON replacement | Temp, flush, permissions, replace, rollback |
| P13 | Exception chaining | Useful user message and preserved cause |
| P14 | Context-manager cleanup | File/lock closes on failure |
| P15 | Secret-safe logging | Redaction and control-character handling |
| P16 | Bounded retry | Only transient idempotent operation |
| P17 | argparse validator | Invalid threshold exits 2 |
| P18 | Text and JSON CLI | Clean stdout/stderr contract |
| P19 | Dry-run configuration plan | No state mutation |
| P20 | Safe subprocess | Args, timeout, env, exit/stderr handling |
| P21 | Missing executable | Translate `FileNotFoundError` |
| P22 | Command timeout | Child/process-group behavior documented |
| P23 | Parse `systemctl show` | Loaded/active/sub/result distinctions |
| P24 | Parse `ip -json` | Address inventory without table parsing |
| P25 | `/proc` process race | Handle vanished PID normally |
| P26 | Byte disk usage | Explicit inode/quota limitations |
| P27 | DNS result inventory | IPv4/IPv6 and duplicate handling |
| P28 | TLS-valid HTTPS check | Correct CA/name/timeout/body bound |
| P29 | Redirect restriction | Prevent allowlist escape |
| P30 | API pagination | Bounded pages and schema validation |
| P31 | SSH log parser | Regex plus IP validation and malformed count |
| P32 | Time normalization | Preserve raw time and derived UTC |
| P33 | Monotonic deadline | Survive wall-clock change conceptually |
| P34 | Threaded URL checks | Eight workers, stable sorted result |
| P35 | Partial fleet failure | Successful hosts retained; exit nonzero |
| P36 | unittest subprocess wrapper | Exact argv/timeout/environment assertions |
| P37 | Build and install wheel | Fresh venv entry points pass |
| P38 | Least-privilege systemd service | Dedicated user and sandbox |
| P39 | systemd timer | Persistent, randomized, observable |
| P40 | Graduation capstone | Inventory + disk + service + HTTPS + tests/deploy |
