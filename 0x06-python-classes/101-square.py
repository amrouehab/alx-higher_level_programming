#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """A class that defines a square with size and position attributes.

    Attributes:
        size (int): The size of the square (side length).
        position (tuple): The position of the square represented by spaces before each line.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with optional size and position.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position for printing the square.
                                        Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square after validation.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square after validation.

        Args:
            value (tuple): The position as a tuple of 2 positive integers.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the character #, accounting for position.

        If size is 0, it prints an empty line.
        The position is used to print spaces before the square's lines.
        """
        if self.__size == 0:
            print()
            return

        # Print new lines based on position[1]
        [print() for _ in range(self.__position[1])]

        # Print the square with spaces based on position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Defines the string representation of the square.

        Returns:
            str: The string to print the square.
        """
        if self.__size == 0:
            return ""

        result = []
        # Add empty lines based on position[1]
        result.append("\n" * self.__position[1])

        # Add each line of the square with spaces based on position[0]
        for _ in range(self.__size):
            result.append(" " * self.__position[0] + "#" * self.__size)
            result.append("\n")

        return "".join(result).rstrip()
