#!/usr/bin/python3
""" Module to load a object from json
"""
import json


def from_json_string(my_str):
    """ Returns the json from a string
    """
    return json.loads(my_str)
