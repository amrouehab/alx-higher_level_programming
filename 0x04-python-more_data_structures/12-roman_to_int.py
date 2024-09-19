#!/usr/bin/python3
"""
Converts a Roman numeral to an integer
"""

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total, prev_value = 0, 0

    for char in roman_string:
        current_value = roman_dict.get(char, 0)
        if current_value > prev_value:
            total += current_value - 2 * prev_value
        else:
            total += current_value
        prev_value = current_value

    return total
