#!/usr/bin/python3
# 1-rectangle.py
# Auth: Shahinda Altayeb

"""class name Rectangle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

        """Retarve height"""
        def width(self):
            return self.__height

        """Git the value of the height"""
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            elif value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

        """Retarve width"""
        def height(self):
            return self.__width

        """Git width value"""
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
