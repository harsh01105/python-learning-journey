import os

folder = "."  # current folder

files = os.listdir(folder)
categories = {}

for file in files:
    if os.path.isfile(file):
        ext = os.path.splitext(file)[1] or "no_extension"
        categories.setdefault(ext, []).append(file)

for ext, file_list in categories.items():
    print(f"{ext}: {file_list}")