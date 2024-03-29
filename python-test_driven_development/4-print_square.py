#!/usr/bin/python3
""" Prints a square with # as chars
"""


def print_square(size):
    """ Prints a square with # as chars
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
