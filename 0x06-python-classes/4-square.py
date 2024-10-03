#!/usr/bin/python3
"""Defines a class Square."""

class Square:
    """A class that defines a square with access and update of size."""
    
    def __init__(self, size=0):
        """Initializes the square, validating that size is an integer >= 0."""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets and validates the size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size ** 2
