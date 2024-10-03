#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """A class that defines a square by size, with validation and area calculation."""
    
    def __init__(self, size=0):
        """Initializes the square, validating that size is an integer >= 0."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
