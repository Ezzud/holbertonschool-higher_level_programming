#!/usr/bin/python3
""" Task 1 file
"""


class MyList(list):
    """ Inherits the attributes of a list"""

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
