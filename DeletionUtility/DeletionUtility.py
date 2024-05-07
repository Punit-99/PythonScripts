import os

def delete_files(folder_path, files_to_delete):
    files = os.listdir(folder_path)
    
    for index, file in enumerate(files):
        print(f"{index + 1}. {file}")

    confirm = input("Enter 'confirm' to delete the listed files: ")

    if confirm.lower() == 'confirm':
        def delete_file(file_idx):
            try:
                os.remove(os.path.join(folder_path, files[file_idx]))
                print(f"Deleted: {files[file_idx]}")
            except FileNotFoundError:
                print(f"File {files[file_idx]} not found.")

        for data in files_to_delete:
            if '-' in data:
                start, end = map(int, data.split('-'))
                for i in range(start, end + 1):
                    delete_file(i - 1)
            else:
                index = int(data) - 1
                delete_file(index)
    else:
        print("Deletion process cancelled.")
if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    data_input = input("Enter the data to delete (separated by comma): ")
    files_to_delete = [x.strip() for x in data_input.split(',')]

    delete_files(folder_path, files_to_delete)

