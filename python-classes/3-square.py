#!/usr/bin/python3
"""3-square.py: Defines a Square class with private instance attribute 'size', size validation, and area method, as well as getter and setter for size."""

class Square:
    """Represents a square."""
    
    def __init__(self, size=0):
        """Initialize a new Square instance."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    
    @property
    def size(self):
        """Retrieve the size attribute."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size attribute."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2

# The following code is for testing purposes
if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
