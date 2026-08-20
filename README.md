

Linux + Bash + Python + Git + GitHub + CI + Testing + Logging + Error Handling.

# Project 1: auto-backup.sh — Bash Script to Backup Files or Folders

A simple and reliable Bash script to create timestamped compressed backups of any file or directory. Ideal for developers, sysadmins, and power users who want quick backups without fancy tools.

### Features

✅ Backs up files or folders
📦 Creates .tar.gz compressed archive
🕓 Adds timestamp to avoid overwriting
📝 Logs all successful backups to backup.log
💥 Handles errors (missing args, path not found)

# auto-backup.sh — Bash Script to Backup Files or Folders

A simple and reliable Bash script to create timestamped compressed backups of any file or directory. Ideal for developers, sysadmins, and power users who want quick backups without fancy tools.

### Features

✅ Backs up files or folders
📦 Creates .tar.gz compressed archive
🕓 Adds timestamp to avoid overwriting
📝 Logs all successful backups to backup.log
💥 Handles errors (missing args, path not found)

### Usage
./auto-backup.sh [source_path] [backup_destination]

#Argument	           Description
source_path	         File or directory to back up
backup_destination	 Folder where backup archive will be saved

### Example

./auto-backup.sh ~/Documents ~/Backups

Creates: ~/Backups/Documents_backup_2025-06-26_11-35-10.tar.gz

Logs entry in backup.log like: [SUCCESS] 2025-06-26 11:35:10 - Backup of '/home/user/Documents' saved as '/home/user/Backups/Documents_backup_2025-06-26_11-35-10.tar.gz'

### Sample Output
Backup completed successfully: /home/user/Backups/Documents_backup_2025-06-26_11-35-10.tar.gz

### Project Structure

auto-backup/
├── auto-backup.sh
├── backup.log
└── README.md
