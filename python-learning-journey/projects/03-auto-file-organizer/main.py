import os
import shutil
import argparse

FILE_CATEGORIES = {
    "pdf": "PDFs",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "txt": "TextFiles",
    "csv": "Spreadsheets",
    "xlsx": "Spreadsheets",
    "py": "PythonScripts",
    "json": "DataFiles",
}


def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"Error: '{folder_path}' does not exist.")
        return

    moved_count = 0
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            ext = filename.split(".")[-1].lower() if "." in filename else "others"
            category = FILE_CATEGORIES.get(ext, "Others")

            dest_folder = os.path.join(folder_path, category)
            os.makedirs(dest_folder, exist_ok=True)

            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"Moved: {filename} -> {category}/")
            moved_count += 1

    print(f"\nDone. Organized {moved_count} file(s).")


def main():
    parser = argparse.ArgumentParser(description="Organize files in a folder by type.")
    parser.add_argument("folder", help="Path to the folder you want to organize")
    args = parser.parse_args()

    organize_folder(args.folder)


if __name__ == "__main__":
    main()