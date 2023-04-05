#!/usr/bin/python3
# 1-rectangle.py

"""Class Rectangel"""


class Rectangle:
    """intilization of the attribute.
    Attributes:
        __width (int): the width of the rectangle.
        __height (int): the height of the rectangle
    """


    def __init__(self, width=0, height=0):
        """Class instance intialization"""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Git the width of rectancle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Git the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Git the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
