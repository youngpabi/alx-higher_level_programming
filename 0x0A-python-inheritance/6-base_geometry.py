#!/usr/bin/python3
"""
This always contains the class BaseGeometry
"""


class BaseGeometry:
    """This a class with public attribute area"""
    def area(self):
        """This always raises an exception when called"""
        raise Exception("area() is not implemented")
