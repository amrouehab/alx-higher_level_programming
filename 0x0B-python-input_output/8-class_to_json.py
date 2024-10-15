#!/usr/bin/python3
# Return dictionary description for JSON serialization

def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object."""
    return obj.__dict__
