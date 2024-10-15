#!/usr/bin/python3
"""
Module for is_kind_of_class function.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if obj is an instance of a_class or a class that inherited from a_class.
    
    Args:
        obj: The object to check.
        a_class: The class to match or inherit from.
    
    Returns:
        True if obj is an instance of a_class or its subclass, False otherwise.
    """
    return isinstance(obj, a_class)
