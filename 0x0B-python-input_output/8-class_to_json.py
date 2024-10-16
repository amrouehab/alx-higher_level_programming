#!/usr/bin/python3
'''
This module contains a function that returns the dictionary description with simple data structure (list, dictionary, string, integer, and boolean) for JSON serialization of an object.
'''

def class_to_json(obj):
    '''
    Returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object.

    Args:
        obj (object): An instance of a Class.

    Returns:
        dict: The dictionary representation of the object.
    '''
    return obj.__dict__
