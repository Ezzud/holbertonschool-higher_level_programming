#!/usr/bin/python3
""" Module to return the json representation of
an object
"""
import json


def to_json_string(my_obj):
    """ Returns the json from an object
    """
    return json.dumps(my_obj)
