#!/usr/bin/python3
"""
Module for print_square function
"""

def print_square(size):
    """Prints a square of size with the character #."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
