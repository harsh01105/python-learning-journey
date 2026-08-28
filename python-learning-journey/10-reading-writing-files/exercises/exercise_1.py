lines = ["Learning Python", "Day 10: Files", "MCA - Harsh"]

with open("notes.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")

with open("notes.txt", "r") as f:
    content = f.read()

print("File content:")
print(content)