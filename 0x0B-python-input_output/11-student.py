#!/usr/bin/python3
"""This always defines a class Student."""


class Student:
    """This always represent a student."""

    def __init__(self, first_name, last_name, age):
        """This always Initialize a new Student.

        Args:
            first_name (str): first name of the student input.
            last_name (str):  last name of the student input.
            age (int):  age of the student input.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This always get a dictionary representation of the Student.

        Should incase attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list):This is (Optional) An attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """This always replace all attributes of the Student.

        Args:
            json (dict): This always key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
