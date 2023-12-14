import os
import zipfile
import shutil

def list_zip_files(path):
    zip_files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.zip')]
    return zip_files

def extract_zip_files(zip_files, extraction_folder):
    for zip_file in zip_files:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extraction_folder)
            print(f"Extracted {zip_file} to {extraction_folder}")

def move_files_from_folders(source_folder, destination_folder):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                print(f"Moving {file} to {destination_folder}")
                shutil.move(file_path, os.path.join(destination_folder, file))

def main():
    user_path = input("Enter the path where ZIP files are located: ")
    extraction_destination = input("Enter the path for extracting ZIP files: ")
    move_destination = input("Enter the destination path for moved files: ")

    zip_files = list_zip_files(user_path)
    extract_zip_files(zip_files, extraction_destination)

    for extracted_folder in os.listdir(extraction_destination):
        folder_path = os.path.join(extraction_destination, extracted_folder)
        if os.path.isdir(folder_path):
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    if os.path.isfile(file_path):
                        print(f"Moving {file} to {move_destination}")
                        shutil.move(file_path, os.path.join(move_destination, file))

if __name__ == "__main__":
    main()
