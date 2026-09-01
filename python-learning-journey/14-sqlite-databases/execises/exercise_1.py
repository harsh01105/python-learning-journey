import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        course TEXT
    )
""")

students = [
    ("Harsh", "MCA"),
    ("Priya", "MCA"),
    ("Aman", "B.Tech")
]

cursor.executemany("INSERT INTO students (name, course) VALUES (?, ?)", students)
conn.commit()

cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

conn.close()