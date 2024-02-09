#!/usr/bin/python3
""" Class for task 2 """


class Rectangle:
    """ Rectangle Class to create """

    def __init__(self, width=0, height=0):
        """ Init the class """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Return the width of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width of the rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return the rectangle height """

        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculate rectangle area """

        return self.width * self.height

    def perimeter(self):
        """ Calculate the perimeter of the rectangle"""

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)
