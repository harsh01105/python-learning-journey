# 11 - Organizing Files

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 11

## Notes
- The `os` module lets you interact with the file system: `os.listdir()`, `os.rename()`, `os.remove()`, `os.mkdir()`.
- The `shutil` module handles higher-level file operations: `shutil.copy()`, `shutil.move()`, `shutil.rmtree()`.
- `os.path.join()` builds file paths safely across operating systems (avoids `/` vs `\` issues).
- `os.path.exists(path)` checks if a file/folder exists before you try to use it.
- `os.path.splitext(filename)` splits a filename into name and extension — useful for sorting files by type.
- Always test file-organizing scripts on a COPY of a folder first — `shutil.move()` and `os.remove()` are permanent and can't be undone easily.