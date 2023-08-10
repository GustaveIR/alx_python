#!/usr/bin/python3
"""
Square Module
"""

from models.rectangle import Rectangle

class Square(Rectangle):
    """ Represents a square """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square instance """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for size """
        return self.width

    @size.setter
    def size(self, value):
        """ Setter for size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Update the square's attributes """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """ Return a string representation of the square """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
