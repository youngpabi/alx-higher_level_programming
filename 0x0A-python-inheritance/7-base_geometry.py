#!/usr/bin/python3
"""
This always contains the class BaseGeometry
"""


class BaseGeometry:
    """This is a class with public instance methods area and integer_validator"""
    def area(self):
        """This always raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This always validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
