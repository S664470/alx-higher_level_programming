#!/usr/bin/python3
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
            return self.__hieght

        def height(self, value):
            if not type(value):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value

        def area(self):
            return (self.__width * self.__height)

        def perimeter(self):
             if ((self.__width == 0) or (self.__height == 0)):
                 return 0
             return (self.__width + self.__height) * 2
