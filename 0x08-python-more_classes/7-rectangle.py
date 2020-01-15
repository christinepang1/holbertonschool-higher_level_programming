#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Initialize an empty class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Rectangle Instantiation"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """String representation"""
        if self.__height == 0 or self.__width == 0:
            return ""
        h = str(self.print_symbol) * self.__width
        rectangle = (h + "\n") * self.__height
        rectangle = rectangle[:-1]
        return rectangle

    def __repr__(self):
        """String representation"""
        r = "Rectangle({}, {})"
        return r.format(str(self.__width), str(self.__height))

    def __del__(self):
        """Delete rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height"""
        if not isinstance(value, int):
            raise TypeError("height must be >= 0")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width
