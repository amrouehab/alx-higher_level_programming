#!/usr/bin/python3
"""
Module for inherits_from function.
"""

def inherits_from(obj, a_class):
    """
    Checks if obj is an instance of a class that inherited from a_class (but not a_class itself).
    
    Args:
        obj: The object to check.
        a_class: The class to match.
    
    Returns:
        True if obj is an instance of a subclass of a_class, False otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
