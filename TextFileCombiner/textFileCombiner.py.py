import os

# Define extensions to ignore (non-text files)
ignore_extensions = [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".svg",
    ".mp3",
    ".wav",
    ".mp4",
    ".avi",
    ".css",
    ".py",
]


# Function to determine if a file should be ignored based on its extension and directory name
def should_ignore(file_path):
    allowed_extensions = [".js", ".html", ".env"]  # Allowed text file extensions
    ignored_directories = [
        "node_modules",
        "utility-functions",
        "HTML",
    ]  # Directories to ignore

    # Check if the file is in an ignored directory
    for directory in ignored_directories:
        if os.path.basename(os.path.dirname(file_path)) == directory:
            return True

    # Check if the file extension is in the list of ignored extensions
    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() in ignore_extensions:
        return True

    # Check if the file extension is not in the list of allowed extensions
    if file_extension.lower() not in allowed_extensions:
        return True

    return False


def combine_files(root_folder):
    output_file = os.path.join(root_folder, "combined.txt")
    with open(output_file, "w", encoding="utf-8") as combined:
        for root, _, files in os.walk(root_folder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if not should_ignore(file_path):
                    try:
                        write_file_contents(combined, file_path, root_folder)
                        combined.write(
                            "=========================\n\n"
                        )  # Separator after each file
                    except UnicodeDecodeError:
                        print(f"Skipping non-UTF-8 encoded file: {file_path}")


def write_file_contents(combined_file, file_path, root_folder):
    with open(file_path, "r", encoding="utf-8") as file:
        combined_file.write(
            f"FILENAME:{os.path.relpath(file_path, start=root_folder)}\n\n"
        )
        combined_file.write(file.read() + "\n\n")


if __name__ == "__main__":
    root_folder = os.path.dirname(
        os.path.abspath(__file__)
    )  # Get the directory where this Python script is located
    combine_files(root_folder)
    print(f"Combined file 'combined.txt' created successfully in {root_folder}.")
