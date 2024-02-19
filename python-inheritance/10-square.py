#!/usr/bin/python3
""" Task 10 file
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that defines a Square from a rectangle shape """
    def __init__(self, size):
        """ Init the square shape """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Returns the area of the shape """
        return super().area()
