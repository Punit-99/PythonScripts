import os
import zipfile
import shutil

def list_zip_files(path):
    zip_files = [os.path.join(path, f) for f in os.listdir(path) if f.lower().endswith('.zip')]
    return zip_files

def extract_zip_files(zip_files, extraction_folder):
    for zip_file in zip_files:
        folder_name = os.path.splitext(os.path.basename(zip_file))[0].strip()
        extraction_path = os.path.join(extraction_folder, folder_name)
        os.makedirs(extraction_path, exist_ok=True)
        
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extraction_path)
            print(f"Extracted {zip_file} to {extraction_path}")

def main():
    user_path = input("Enter the path where ZIP files are located: ").strip()
    extraction_destination = input("Enter the path for extracting ZIP files: ").strip()

    zip_files = list_zip_files(user_path)
    if not zip_files:
        print("No ZIP files found in the specified directory.")
        return

    print("Extracting files...")
    extract_zip_files(zip_files, extraction_destination)
    print("Extraction complete.")

if __name__ == "__main__":
    main()
