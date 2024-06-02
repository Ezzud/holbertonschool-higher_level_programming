#!/usr/bin/env python3
""" Module that serialize and deserialize objects 
"""
import pickle


class CustomObject:
    """Object to be serialized and deserialized"""

    def __init__(self, name, age, is_student):
        """CustomObject constructor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display attributes of objects"""
        print("Name:", self.name)
        print("Age:", self.age)
        print("Is Student:", self.is_student)
    
    def serialize(self, filename):
        """Serialize object to file"""
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except Exception:
            return None
         
    @classmethod
    def deserialize(cls, filename):
        """Deserialize object to file"""
        try:        
            with open(filename, "rb") as file:
                return pickle.load(file)
        except Exception:
            return None
