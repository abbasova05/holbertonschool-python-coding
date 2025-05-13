#!/usr/bin/python3
"""
This module defines a class Square that represents a geometric square.
"""

class Square:
    """
    Represents a square.

    This class defines a square by its size, which is a private attribute.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
