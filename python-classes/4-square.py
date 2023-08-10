#!/usr/bin/python3
"""4-square.py: Defines a Square class with private instance attribute 'size', size validation, area method, and my_print method."""

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
    
    def my_print(self):
        """Print the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

# The following code is for testing purposes
if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
