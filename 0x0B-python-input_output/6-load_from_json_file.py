#!/usr/bin/python3
import json

def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the file to load the JSON representation from.

    Returns:
        object: The Python data structure represented by the JSON string in the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
