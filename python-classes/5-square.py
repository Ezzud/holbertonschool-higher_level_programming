#!/usr/bin/python3
class Square:
    """ Square Class
    """
    def __init__(self, size=0):
        """ Init square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Return square of object
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ Return size value
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Set size and object
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """ Print square with #
        """
        if not self.__size:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()
