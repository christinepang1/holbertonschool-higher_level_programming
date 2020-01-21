#!/usr/bin/python3
"""Class BaseGeometry"""


class BaseGeometry:
    """Empty Class BaseGeometry"""
    def area(self):
        """Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Ensures integer"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Class Rectangle"""
    def __init__(self, width, height):
        """Init width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns Rectangle's area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size):
        """Init Square"""
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Area of Square"""
        return self.__size ** 2

    def __str__(self):
        """Representation of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
