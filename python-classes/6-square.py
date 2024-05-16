#!/usr/bin/python3
"""Task 6 for Square class"""


class Square:
    """ Class that create a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Class that create a square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Return size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the object"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Return position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ Set position and object of the class"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Return square of the object"""
        return (self.__size ** 2)

    def my_print(self):
        """ Print a square with # based on position and size"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for k in range(self.position[0]):
                    print(" ", end='')
                for j in range(self.size):
                    print("#", end='')
                print()
