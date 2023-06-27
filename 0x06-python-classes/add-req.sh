#!/bin/bash

# Check if a filename was provided as a command line argument
if [ $# -lt 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

filename=$1

# Create a temporary file
temp_file=$(mktemp)

# Add the specified string to the top of the temporary file
echo '#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""
    
' > $temp_file

# Append the contents of the original file to the temporary file
cat $filename >> $temp_file

# Replace the original file with the temporary file
mv $temp_file $filename
