#!/usr/bin/python3
"""
Module for Rectangle class.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
