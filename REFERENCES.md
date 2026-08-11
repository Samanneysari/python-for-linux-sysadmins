# Official References

- [Python documentation](https://docs.python.org/3/)
- [Python tutorial](https://docs.python.org/3/tutorial/)
- [Python standard library](https://docs.python.org/3/library/)
- [`pathlib`](https://docs.python.org/3/library/pathlib.html)
- [`subprocess`](https://docs.python.org/3/library/subprocess.html)
- [`logging`](https://docs.python.org/3/library/logging.html)
- [`argparse`](https://docs.python.org/3/library/argparse.html)
- [`unittest`](https://docs.python.org/3/library/unittest.html)
- [`venv`](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Installing packages with venv and pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- [Externally managed environments](https://packaging.python.org/en/latest/specifications/externally-managed-environments/)
- [Packaging Python projects](https://packaging.python.org/tutorials/packaging-projects/)
- [PEP 8 style guide](https://peps.python.org/pep-0008/)
- [Python security considerations](https://docs.python.org/3/library/security_warnings.html)

Read documentation for the interpreter actually running:

```bash
python3 --version
python3 -m pydoc pathlib
python3 -m pip --version
```

Do not use `sudo pip install` against the distribution interpreter. Use distribution packages, a project virtual environment, or an approved standalone-application mechanism.
