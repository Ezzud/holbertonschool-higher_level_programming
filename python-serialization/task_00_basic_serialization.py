#!/usr/bin/env python3
""" Module that contains functions of basic serialization
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize and save to file"""

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load file and deserialize"""

    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
