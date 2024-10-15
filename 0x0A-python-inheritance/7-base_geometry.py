#!/usr/bin/python3
"""
Module for BaseGeometry class.
"""

class BaseGeometry:
    """
    A class BaseGeometry with area and integer_validator methods.
    """

    def area(self):
        """
        Raises an Exception with message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that value is a positive integer.
        
        Args:
            name: A string representing the name of the value.
            value: The value to be validated.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
