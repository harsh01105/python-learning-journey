# 09 - Regular Expressions

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 9

## Notes
- Regex (regular expressions) let you search for patterns in text, not just exact matches.
- Use the `re` module: `import re`
- `re.search(pattern, text)` finds the first match; `re.findall(pattern, text)` finds ALL matches.
- `re.sub(pattern, replacement, text)` replaces matches with something else.
- Common pattern symbols:
  - `\d` = digit, `\w` = word character, `\s` = whitespace
  - `+` = one or more, `*` = zero or more, `?` = optional
  - `()` = grouping, `|` = OR
- Use **raw strings** for patterns: `r"\d+"` (avoids escape-character confusion).
- `.group()` extracts the matched text from a `re.search()` result.