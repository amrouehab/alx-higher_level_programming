#!/usr/bin/python3
import json


class Rectangle:
    """A class that defines a rectangle."""
    instance_count = 0  # Class variable to count instances

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.instance_count += 1  # Increment instance count

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle for eval."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message when an instance is deleted."""
        Rectangle.instance_count -= 1  # Decrement instance count
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with the larger area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            'width': self.__width,
            'height': self.__height
        }

    @staticmethod
    def save_to_file(rectangles):
        """Save a list of rectangles to a file in JSON format."""
        with open("Rectangle.json", "w") as f:
            if rectangles is None:
                f.write("[]")
            else:
                json.dump([rect.to_dictionary() for rect in rectangles], f)
