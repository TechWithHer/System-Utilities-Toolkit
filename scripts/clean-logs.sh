#!/bin/bash

echo "Starting log cleanup..."

# Check that 3 arguments were provided
if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <directory> <file-pattern> <days>"
    exit 1
fi

DIRECTORY="$1"
PATTERN="$2"
DAYS="$3"

# Check if directory exists
if [ ! -d "$DIRECTORY" ]; then
    echo "Error: Directory does not exist: $DIRECTORY"
    exit 1
fi

echo "Cleaning files older than $DAYS days..."

find "$DIRECTORY" -type f -name "$PATTERN" -mtime +"$DAYS" -print -delete

echo "Cleanup completed."