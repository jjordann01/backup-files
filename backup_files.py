import os
import shutil
from datetime import datetime

def backup_files(source_dir, backup_dir):
    # Ensure that source and destination directories exist
    if not os.path.exists(source_dir):
        print(f"Source directory {source_dir} does not exist.")
        return
    if not os.path.exists(backup_dir):
        print(f"Destination directory {backup_dir} does not exist. Creating it now.")
        os.makedirs(backup_dir)

    # Get the current date for naming the backup folder
    current_date = datetime.now().strftime("%Y-%m-%d")
    backup_folder = os.path.join(backup_dir, f"backup_{current_date}")
    
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
        print(f"Created backup folder: {backup_folder}")

    # Iterate over the source directory and copy files to the backup folder
    for foldername, subfolders, filenames in os.walk(source_dir):
        # Get the relative path of the current folder inside the source directory
        relative_path = os.path.relpath(foldername, source_dir)
        
        # Create the same folder structure in the backup location
        backup_subfolder = os.path.join(backup_folder, relative_path)
        
        # Create the folder if it doesn't exist
        if not os.path.exists(backup_subfolder):
            os.makedirs(backup_subfolder)
        
        # Copy all files in the current folder
        for filename in filenames:
            source_file = os.path.join(foldername, filename)
            destination_file = os.path.join(backup_subfolder, filename)

            # Check if the file already exists in the backup folder
            if not os.path.exists(destination_file):
                print(f"Backing up: {source_file} to {destination_file}")
                shutil.copy2(source_file, destination_file)
            else:
                print(f"Skipping: {source_file} already exists in backup.")

if __name__ == "__main__":
    source_dir = input("Enter the path to the source directory: ")
    backup_dir = input("Enter the path to the backup directory: ")
    backup_files(source_dir, backup_dir)

