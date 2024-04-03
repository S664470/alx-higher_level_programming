#!/usr/bin/python3
""" Size validation"""


class Square:
    """class function and attribute intilization"""

    def __init__(self, size=0, position=(0,0)):
        self.__size = size
        self.position = position

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size) ** 2

    @property
    def size(self):
        """reterve size"""

        return self.__size

    @size.setter
    def size(self, value):
        """instance method to set value"""

        self.value = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """print in stdout square of "#" """

        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))

    def position(self):
        self.__position = position

        @position.setter
        def position(self, value):
            """
            To set the position size
            position int
            """

            if not isinstance(position, tuple) or len(value) != 2 or not isinstance(value, int) or not isinstance(position, int):
                raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

            for i in range(self.__position[1]):
                print()
                return
            for i in range(self.__size):
                print("" * self.__position[0] + "#" * self.__size)
