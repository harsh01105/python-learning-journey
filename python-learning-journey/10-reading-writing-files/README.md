# 10 - Reading and Writing Files

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 10

## Notes
- Open a file with `open(filename, mode)`. Common modes: `"r"` (read), `"w"` (write, overwrites), `"a"` (append).
- Always use `with open(...) as f:` — it auto-closes the file, even if an error happens.
- `.read()` reads the whole file as one string; `.readlines()` reads it as a list of lines.
- `f.write(text)` writes text to a file (doesn't add a newline automatically — add `\n` yourself).
- File paths can be relative (`"data.txt"`) or absolute (`"C:/Users/.../data.txt"`).
- Writing with mode `"w"` will **erase** the existing file content first — use `"a"` if you want to add to it instead.
- The `os.path` module (used more in Chapter 11) helps you check if a file/folder exists before opening it.