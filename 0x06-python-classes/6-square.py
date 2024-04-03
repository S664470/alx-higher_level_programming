#!/usr/bin/python3
""" Size validation"""


class Square:
    """class function and attribute intilization"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculate area"""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
            return

        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print()

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
