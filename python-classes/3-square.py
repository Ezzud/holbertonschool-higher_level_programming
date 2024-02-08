#!/usr/bin/python3
"""Task 3 for Square class"""


class Square:
    def __init__(self, size=0):
        """ Class that create a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return square of the object
        """
        return (self.__size ** 2)
