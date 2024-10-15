#!/usr/bin/python3
# Save an object to a file in JSON format

import json

def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using its JSON representation."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
