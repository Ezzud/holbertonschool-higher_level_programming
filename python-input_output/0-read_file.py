#!/usr/bin/python3
""" Module to read from a file """


def read_file(filename=""):
    """ Read from a file
    """

    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
