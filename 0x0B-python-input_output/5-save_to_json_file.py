#!/usr/bin/python3
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.

    Args:
        my_obj (object): The object to be serialized to JSON and saved to a file.
        filename (str): The name of the file to save the JSON representation.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
