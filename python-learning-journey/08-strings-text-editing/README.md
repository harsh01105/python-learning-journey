# 08 - Strings and Text Editing

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 8

## Notes
- Strings are immutable — methods like `.upper()` return a NEW string, they don't change the original.
- Common methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`, `.replace()`, `.find()`, `.startswith()`, `.endswith()`.
- Slicing works on strings too: `my_str[0:3]`
- f-strings (`f"{variable}"`) are the modern way to format text — can also format numbers: `f"{price:.2f}"`
- `.split()` turns a string into a list; `"".join(list)` turns a list back into a string.
- `in` checks if a substring exists: `"cat" in "concatenate"`
- Escape characters: `\n` (newline), `\t` (tab), `\\` (backslash), `\"` (quote inside a string).

This wraps up **Part I — Programming Fundamentals**. From Day 9 we move into Part II (automation topics: regex, files, web scraping, etc.).