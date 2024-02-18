#!/usr/bin/python3
""" Module of the Student class
"""


class Student:
    """ Class to create a student """

    def __init__(self, first_name, last_name, age):
        """ Init the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Convert it to json """
        return self.__dict__.copy()
