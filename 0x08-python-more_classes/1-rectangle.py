#!/usr/bin/python3
# Auth: Shahinda Altayeb
class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width
    def width(self, value):
        if not type(value):
             raise TypeError("width must be an integer")
        if value < 0:
             raise ValueError("width must be >= 0")
             self.__width = value

    def height(self):
        return self.__height
    def height(self, value):
        if not type(value):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
            self.__height = value
