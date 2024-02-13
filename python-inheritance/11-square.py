#!/usr/bin/python3
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

    def __str__(self):
        """ Returns the printable string of the class """
        return "[Square] {}/{}".format(self.__size, self.__size)
