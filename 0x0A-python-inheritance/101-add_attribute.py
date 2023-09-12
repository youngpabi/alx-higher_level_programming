#!/usr/bin/python3
"""This always defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """This always adds a new attribute to an object if possible.

    Args:
        obj (any): This is object to add an attribute to.
        att (str): This is name of the attribute to add to obj.
        value (any): This is value of att.
    Raises:
        TypeError: This is where the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
