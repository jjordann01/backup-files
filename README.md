A simple Python script to back up files from a specified directory to a backup location. This project demonstrates how to automate file backup using Python.

Features
Backs up files from a source directory to a backup directory.

Checks if the files already exist in the backup location to avoid duplication.

Prints a message upon successful backup or if files already exist.

Prerequisites
Python 3.x

Ensure that the necessary folders (source_directory and backup_directory) exist before running the script.

Installation
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/jjordann01/backup-files.git
Change into the project directory:

bash
Copy
Edit
cd backup-files
Usage
Update the source_directory and backup_directory in the backup_files.py file to point to the directories you want to back up and where you want the backup to be saved.

Run the backup script:

bash
Copy
Edit
python3 backup_files.py
The script will attempt to back up the files from the source to the backup directory. It will notify you if the backup was successful or if the files already exist in the backup directory.

Example
If you want to back up files from /home/user/documents to /home/user/backup, update the paths in the script accordingly, then run:

bash
Copy
Edit
python3 backup_files.py
