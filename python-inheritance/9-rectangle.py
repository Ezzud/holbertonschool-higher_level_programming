#!/usr/bin/python3
""" Task 9 file
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that defines a rectangle based of a shape """

    def __init__(self, width, height):
        """ Init the instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of the instance """
        return self.__width * self.__height

    def __str__(self):
        """ Return the printable of the class """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
