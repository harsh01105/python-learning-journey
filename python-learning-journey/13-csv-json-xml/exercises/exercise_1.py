import csv

books = [
    {"title": "A Light in the Attic", "price": "£51.77"},
    {"title": "Tipping the Velvet", "price": "£53.74"},
    {"title": "Soumission", "price": "£50.10"},
]

with open("books.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price"])
    writer.writeheader()
    writer.writerows(books)

with open("books.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)