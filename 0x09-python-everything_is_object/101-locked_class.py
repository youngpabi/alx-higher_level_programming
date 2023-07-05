#!/usr/bin/python3
"""
    101-locked_class:This is class LockedClass
"""


class LockedClass:
    """
        This is the class that  only have one attribute first_name.
        Attribute:
             first_name (str): name
    """
    __slots__ = ['first_name']
