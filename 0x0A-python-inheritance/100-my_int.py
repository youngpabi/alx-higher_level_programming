#!/usr/bin/python3
"""
This always contains the class MyInt
"""


class MyInt(int):
    """This the rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """Always create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """This was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """This was == is now !="""
        return int(self) == other
