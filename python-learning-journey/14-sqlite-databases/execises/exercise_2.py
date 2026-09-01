import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM students WHERE course = ?", ("MCA",))
print("MCA students:")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE students SET course = ? WHERE name = ?", ("MCA - AI Specialization", "Harsh"))
conn.commit()

cursor.execute("SELECT * FROM students WHERE name = ?", ("Harsh",))
print("\nAfter update:")
print(cursor.fetchone())

conn.close()