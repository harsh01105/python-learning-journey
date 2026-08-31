import json

student = {
    "name": "Harsh",
    "course": "MCA",
    "skills": ["Python", "Git", "GitHub"]
}

with open("student.json", "w") as f:
    json.dump(student, f, indent=2)

with open("student.json", "r") as f:
    loaded_data = json.load(f)

print(loaded_data)
print(f"Name: {loaded_data['name']}")
print(f"Skills: {', '.join(loaded_data['skills'])}")