#!/usr/bin/python3
"""
Module for MyList class that extends the built-in list.
"""

class MyList(list):
    """
    A subclass of list that can print the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
