#!/bin/bash

set -euo pipefail

#Check Number of Arguments 

$SOURCE="$1"
$DESTINATION="$2"
TimeStamp=$(date +"%Y-%m-%d_%H-%M-%S")
BASENAME=$(basename "$SOURCE")
BACKUP_NAME="${BASENAME}_backup_${TIMESTAMP}.tar.gz"
LOG_FILE="backup.log"   
if [ "$#" -ne 2 ]; then
 echo "Usage: $0 [source_path] [backup_destination]"
 exit 1 
fi
if [ ! -e "$SOURCE" ]; then
  echo "[ERROR] Source path does not exist: $SOURCE"
  exit 2
fi
mkdir -p "$DESTINATION"
tar -czf "$DESTINATION/$BACKUP_NAME" "$SOURCE"
echo "[SUCCESS] $(date +"%F %T") - Backup of '$SOURCE' saved as '$DESTINATION/$BACKUP_NAME'" >> "$LOG_FILE"
echo "Backup completed successfully: $DESTINATION/$BACKUP_NAME" 
