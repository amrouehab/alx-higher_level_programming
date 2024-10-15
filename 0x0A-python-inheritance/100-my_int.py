#!/usr/bin/python3
"""
Module for MyInt class that inverts == and != operators.
"""

class MyInt(int):
    """
    A rebel version of int where == and != are inverted.
    """

    def __eq__(self, other):
        """
        Overrides == operator with != behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides != operator with == behavior.
        """
        return super().__eq__(other)
