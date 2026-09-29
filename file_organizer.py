import os
import shutil
import logging

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Python": [".py"],
    "Other": []
}


def get_category(filename):
    extension = os.path.splitext(filename)[1].lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Other"


def organize_files(folder_path):

    print("\nStarting file organization...")

    try:
        if not os.path.exists(folder_path):
            print("Error: Folder does not exist.")
            logging.error("Folder does not exist: %s", folder_path)
            return

        files = os.listdir(folder_path)

        for filename in files:

            source_path = os.path.join(folder_path, filename)

            if os.path.isdir(source_path):
                continue

            category = get_category(filename)

            category_folder = os.path.join(folder_path, category)
            if not os.path.exists(category_folder):
                os.makedirs(category_folder)

            destination_path = os.path.join(category_folder, filename)

            shutil.move(source_path, destination_path)

            print(f"Moved: {filename} → {category}/")
            logging.info("Moved %s to %s", filename, category)

        print("\nFile organization completed successfully.")

    except Exception as e:
        print("An error occurred:", e)
        logging.error("Error while organizing files: %s", e)


def rename_files(folder_path):

    print("\nRename Files")
    print("-" * 30)

    try:
        prefix = input("Enter a prefix for the files: ").strip()

        if prefix == "":
            print("Prefix cannot be empty.")
            return

        files = os.listdir(folder_path)
        count = 1

        for filename in files:

            file_path = os.path.join(folder_path, filename)

            if os.path.isfile(file_path):

                extension = os.path.splitext(filename)[1]

                new_name = f"{prefix}_{count}{extension}"

                new_path = os.path.join(folder_path, new_name)

                os.rename(file_path, new_path)

                print(f"Renamed: {filename} → {new_name}")
                logging.info("Renamed %s to %s", filename, new_name)

                count += 1

        print("\nRenaming completed successfully.")

    except Exception as e:
        print("An error occurred:", e)
        logging.error("Error while renaming files: %s", e)


def clean_empty_folders(folder_path):

    print("\nCleaning empty folders...")

    try:
        removed = 0

        for item in os.listdir(folder_path):

            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):

                if not os.listdir(item_path):
                    os.rmdir(item_path)

                    print(f"Removed empty folder: {item}")
                    logging.info("Removed empty folder: %s", item)

                    removed += 1

        print(f"\nCleaning completed. {removed} empty folder(s) removed.")

    except Exception as e:
        print("An error occurred:", e)
        logging.error("Error while cleaning folders: %s", e)

def main():

    print("=" * 50)
    print("       PYTHON FILE AUTOMATION TOOL")
    print("=" * 50)

    folder_path = input("\nEnter the folder path to organize: ").strip()

    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        logging.error("Invalid folder path: %s", folder_path)
        return

    while True:

        print("\nChoose an operation:")
        print("1. Organize files")
        print("2. Rename files")
        print("3. Clean empty folders")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            organize_files(folder_path)

        elif choice == "2":
            rename_files(folder_path)

        elif choice == "3":
            clean_empty_folders(folder_path)

        elif choice == "4":
            print("\nThank you for using the File Automation Tool!")
            logging.info("Program exited by user.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
