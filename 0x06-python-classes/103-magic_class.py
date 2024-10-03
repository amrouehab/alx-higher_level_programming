#!/usr/bin/python3
"""
This module defines a MagicClass that replicates Python bytecode.
"""

import math


class MagicClass:
    """Defines a circle."""
    def __init__(self, radius=0):
        """
        Initializes the circle with a given radius.

        Args:
            radius (int, float): Radius of the circle. Must be a number.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates the circumference of the circle."""
        return 2 * math.pi * self.__radius
