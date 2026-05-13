import os
import shutil

def organize_files(folder_path):
    # Dictionary mapping file extensions to folder names
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Archives": [".zip", ".rar", ".tar"],
        "Scripts": [".py", ".js", ".sh"]
    }

    # Create folders if they don't exist
    for folder in file_types.keys():
        folder_dir = os.path.join(folder_path, folder)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

    # Move files into respective folders
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            for folder, extensions in file_types.items():
                if ext.lower() in extensions:
                    shutil.move(file_path, os.path.join(folder_path, folder, filename))
                    print(f"Moved: {filename} → {folder}")
                    break

if __name__ == "__main__":
    target_folder = input("Enter the folder path to organize: ")
    organize_files(target_folder)
    print("✅ Files organized successfully!")
