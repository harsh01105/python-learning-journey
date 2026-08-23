# 05 - Debugging

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 5

## Notes
- **Exceptions** are errors that occur while a program runs (e.g. `ZeroDivisionError`, `ValueError`).
- `try` / `except` lets you catch an exception instead of crashing the program.
- You can catch specific exception types: `except ValueError:` vs a generic `except Exception:`.
- `finally` runs no matter what — useful for cleanup code.
- `assert condition, "message"` stops the program if `condition` is `False` — used to catch bugs early during development.
- A **traceback** shows exactly where and why an error happened — always read it bottom to top.
- `raise` lets you manually trigger an exception when something is wrong.