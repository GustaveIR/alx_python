#!/usr/bin/python3

class Square:
    """
    A class that defines a square by a private instance attribute 'size'.

    Attributes:
        size (int): The size of the square.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
