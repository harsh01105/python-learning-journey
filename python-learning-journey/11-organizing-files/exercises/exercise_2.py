import os
import shutil

folder = "test_files"  # a sample folder you create with a few dummy files to test on

if os.path.exists(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].replace(".", "") or "others"
            dest_folder = os.path.join(folder, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(dest_folder, file))
            print(f"Moved {file} -> {ext}/")
else:
    print(f"Folder '{folder}' not found. Create it with a few test files first.")