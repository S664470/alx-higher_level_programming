#!/usr/bin/python3
"""
class rectangle inharet from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """rectangle class instance"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width

        self.integer_validator("height", height)
        self.__height = height

        if not isinstance(height, int):
            raise TypeError("[TypeError] height must be an integer")
