# 14 - SQLite Databases

**Book chapter:** Automate the Boring Stuff with Python, 3rd Ed. — Chapter 16

## Notes
- SQLite is a lightweight, file-based database — no separate server needed, perfect for learning and small projects.
- Python's built-in `sqlite3` module connects to it: `sqlite3.connect("mydata.db")`
- A `.db` file is created automatically the first time you connect to a new database name.
- You need a `cursor` to run SQL commands: `cursor = conn.execute(...)` or `conn.cursor()`.
- Basic SQL you'll use: `CREATE TABLE`, `INSERT INTO`, `SELECT`, `UPDATE`, `DELETE`.
- Always call `conn.commit()` after changes (INSERT/UPDATE/DELETE) to actually save them to the file.
- Use `?` placeholders in queries (not f-strings) to avoid SQL injection: `cursor.execute("INSERT INTO users VALUES (?, ?)", (name, age))`
- Close the connection when done: `conn.close()` (or use `with sqlite3.connect(...) as conn:`).