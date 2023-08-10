#!/usr/bin/python3
"""2-square.py: Defines a Square class with private instance attribute 'size', size validation, and area method."""

class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initialize a new Square instance."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    
    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

# The following code is for testing purposes
if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
