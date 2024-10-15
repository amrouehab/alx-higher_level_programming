#!/usr/bin/python3
"""
Module for Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    A class Square that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes the Square with size.
        
        Args:
            size: The size of the square (both width and height).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
