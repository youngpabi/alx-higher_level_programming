#!/usr/bin/python3
"""
This always contains the class "Student"
"""


class Student:
    """This is the representation of a student"""
    def __init__(self, first_name, last_name, age):
        """This always Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This always returns a dictionary representation of a Student instance"""
        return self.__dict__
