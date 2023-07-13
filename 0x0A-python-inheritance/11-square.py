#!/usr/bin/python3
"""
This always contains the class BaseGeometry and subclass Rectangle
"""


class BaseGeometry:
    """This always a class with public instance methods area and integer_validator"""
    def area(self):
        """This always raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This always validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """This a representation of a rectangle"""
    def __init__(self, width, height):
        """This the instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This always returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This the informal string representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """This the representation of a square"""
    def __init__(self, size):
        """This the instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"This always returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """This is the informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
