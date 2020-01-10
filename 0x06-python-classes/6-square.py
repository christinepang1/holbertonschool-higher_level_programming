#!/usr/bin/python3
"""Define a class Square"""


class Square():
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square"""
        self.size = size
        self.position = position

    @property  # getter
    def size(self):
        """Size of the square"""
        return self.__size  # this is a private instance

    @size.setter  # setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return area of square"""
        return self.__size ** 2

    def my_print(self):
        """Print square"""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
