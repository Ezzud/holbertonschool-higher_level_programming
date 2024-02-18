#!/usr/bin/python3
""" Module save a json to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """ Write JSON of an object to a text file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
