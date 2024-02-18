#!/usr/bin/python3
""" Class for task 9 """


class Rectangle:
    """ Rectangle Class to create """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Init the class """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Get the rectangle with # """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += (str(self.print_symbol) * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ Return string representation of the instance """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Return a message when instance is deleted """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns the bigger rectangle """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ Return a new instance of the class """

        return cls(size, size)
