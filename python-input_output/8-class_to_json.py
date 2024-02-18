#!/usr/bin/python3
""" Module that return the dict to json
"""


def class_to_json(obj):
    """ Returns the dictionary of obj """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
