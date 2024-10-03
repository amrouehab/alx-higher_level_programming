#!/usr/bin/python3
"""
This module defines a Square class with comparison operators.
"""

class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """
        Initializes a new Square.

        Args:
            size (int, float): The size of the square (must be >= 0).
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Defines equality comparison based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defines inequality comparison based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defines less than comparison based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Defines less than or equal comparison based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defines greater than comparison based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defines greater than or equal comparison based on area."""
        return self.area() >= other.area()
