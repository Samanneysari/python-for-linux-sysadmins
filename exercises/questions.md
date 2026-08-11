# Exercises

1. When is Bash better than Python for administration?
2. Why avoid modifying the distribution Python with `sudo pip`?
3. What does a virtual environment isolate and share?
4. Why invoke pip as `python -m pip`?
5. What does venv activation change?
6. Why should systemd call an absolute interpreter/entry point?
7. What does the module guard prevent?
8. Why return an integer from `main`?
9. What does `py_compile` prove?
10. Compare editable install and production artifact.
11. Compare `str` and `bytes`.
12. Why use explicit encoding/error policy?
13. Compare list, set, dict, and tuple.
14. Why can shallow copy mutate original nested data?
15. Distinguish `None`, zero, empty string, and False.
16. Compare `==` and `is`.
17. Why sort operational output?
18. When should a comprehension become a loop?
19. Why not modify a dict while iterating it?
20. When should `Decimal` replace float?
21. Define a pure function.
22. Why validate inside a function?
23. Why are mutable default arguments shared?
24. What do type hints enforce at runtime?
25. What does frozen dataclass not protect?
26. Why avoid work at import time?
27. What does passing `argv` improve?
28. Why split command execution from parsing?
29. What is dependency injection?
30. Why preserve an exception cause?
31. Why use pathlib?
32. Why is a resolved path not authorization?
33. Why stream large files?
34. Why avoid bare `rstrip()` for fixed-format lines?
35. Why does JSON parsing not validate a schema?
36. Why open CSV with `newline=""`?
37. What is CSV formula injection?
38. Why can mode bits be incomplete access evidence?
39. What does atomic replace provide and miss?
40. Why is pickle unsafe for untrusted data?
41. When should an exception be caught?
42. Why catch specific exceptions?
43. What does a context manager guarantee?
44. Why should libraries not call `basicConfig`?
45. Which data must not be logged?
46. How can log injection occur?
47. Which errors are retryable?
48. Why use jitter with backoff?
49. How should partial failure affect exit/output?
50. Why separate debug traceback from normal error output?
51. Why validate CLI values during parsing?
52. Why separate stdout and stderr?
53. What belongs in machine-readable output?
54. Why is `--yes` not a full safety control?
55. What should dry-run prove?
56. How can symlink races defeat path checks?
57. Why document exit codes?
58. Why reject option-like resource names?
59. What does `subprocess.run(check=True)` do?
60. Why use an argument list?
61. When might `shell=True` be justified?
62. Why set subprocess timeout?
63. What risks exist in `capture_output=True`?
64. Why control environment and locale?
65. Why prefer JSON/machine output from commands?
66. What should an error report preserve about a command?
67. Why can killing a timed-out child be incomplete?
68. Why avoid arbitrary sudo from Python?
69. Compare `pwd` and `getent`.
70. What does `shutil.disk_usage` miss?
71. Why can `/proc/<PID>` disappear?
72. Why is a systemd active service not necessarily healthy?
73. Why parse rather than source `/etc/os-release`?
74. What inventory scope limitations should be declared?
75. What does `getaddrinfo` test?
76. Why can TCP connect pass while HTTPS fails?
77. Why use the default TLS context?
78. How can a URL checker create SSRF?
79. Why restrict redirects and response size?
80. What API fields and errors must be validated?
81. Why prefer structured logs over regex?
82. What risks exist in complex regex on untrusted input?
83. Why validate regex-captured IPs?
84. Why use timezone-aware datetime?
85. Why use monotonic clocks for duration?
86. What breaks a naive file follower?
87. How can cardinality exhaust a log analyzer?
88. Why begin sequentially?
89. What workloads fit threads?
90. What workloads fit process pools?
91. Why can blocking I/O freeze asyncio?
92. What is backpressure?
93. Why sort concurrent results?
94. What belongs in unit, integration, and end-to-end tests?
95. Why test failure paths?
96. What is dependency confusion?
97. What makes a change idempotent?
98. Why separate privilege?
99. What should systemd monitoring distinguish?
100. Define acceptance criteria for the graduation capstone.
