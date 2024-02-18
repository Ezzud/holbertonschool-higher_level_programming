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

    def to_json(self, attrs=None):
        """ Returns the description of dictionaries """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d_list = {}

            for iatr in range(len(attrs)):
                for satr in obj:
                    if attrs[iatr] == satr:
                        d_list[satr] = obj[satr]
            return d_list

        return obj

    def reload_from_json(self, json):
        """ Replace values using a json """
        for atr in json:
            self.__dict__[atr] = json[atr]
