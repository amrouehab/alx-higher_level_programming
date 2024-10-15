#!/usr/bin/python3
# Inserts a line of text after each line containing a specific string

def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specific string."""
    lines = []
    
    # Read the file
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Insert new_string after each matching line
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
