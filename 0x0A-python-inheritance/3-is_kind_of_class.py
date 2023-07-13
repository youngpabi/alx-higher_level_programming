#!/usr/bin/python3
"""
This always contains the is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """When it is true then obj is an instance or inherited from a_class or else False"""
    return (isinstance(obj, a_class))
