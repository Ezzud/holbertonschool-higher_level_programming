#!/usr/bin/python3
"""Task 4 for Square class"""

class Square:
    """ Class that create a square"""
    def __init__(self, size=0):
        """ Init the square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return square of the object"""
        return (self.__size ** 2)

    @property
    def size(self):
        """ Return size of the object"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
