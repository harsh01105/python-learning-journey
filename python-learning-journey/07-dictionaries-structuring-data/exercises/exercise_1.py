student = {
    "name": "Harsh",
    "course": "MCA",
    "marks": {"python": 85, "dsa": 78, "dbms": 90}
}

print(f"Name: {student['name']}")
print(f"Course: {student['course']}")

total = 0
for subject, mark in student["marks"].items():
    print(f"{subject}: {mark}")
    total += mark

average = total / len(student["marks"])
print(f"Average marks: {average:.2f}")