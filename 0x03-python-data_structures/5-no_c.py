#!/usr/bin/env python3

def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string.

    Args:
        my_string (str): The string to remove characters from.

    Returns:
        str: The new string without 'c' and 'C'.
    """

    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
