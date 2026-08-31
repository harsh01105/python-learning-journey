# 13 - CSV, JSON, and XML Files

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 18

## Notes
- **CSV** (Comma-Separated Values) stores tabular data as plain text — handled with Python's built-in `csv` module.
- `csv.writer(file)` writes rows; `csv.DictWriter` writes rows using dictionaries with named columns.
- `csv.reader(file)` reads rows as lists; `csv.DictReader` reads rows as dictionaries (uses the header row as keys).
- **JSON** (JavaScript Object Notation) maps closely to Python dicts/lists — handled with the built-in `json` module.
- `json.dump(data, file)` writes a Python object to a JSON file; `json.load(file)` reads JSON back into Python.
- `json.dumps(data)` converts to a JSON *string* (useful for printing/debugging); `json.loads(string)` parses one.
- XML is more verbose and less common now for simple data — usually only needed for specific APIs/legacy systems (not covered deeply here).