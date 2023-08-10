#!/usr/bin/python3
"""0-square.py: Defines a Square class with private instance attribute 'size'."""

class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square instance."""
        self.__size = size

# The following code is for testing purposes
if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
