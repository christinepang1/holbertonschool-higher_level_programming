#!/usr/bin/python3
"""Rectangle Class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle inherits from class Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        Displays rectangle dimensions:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        r = "[Rectangle] ({}) {}/{} - {}/{}"
        return r.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for x"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """Prints rectangle to stdout using #"""
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def update(self, *args, **kwargs):
        """
        Assigns a key/value argument to attributes.
        Each key in this dictionary represents an attribute to the instance
        """
        if len(args) == 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
            return
        if args is not None and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]
                return
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
                return
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                return
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                return
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
                return

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle"""
        d = {}
        d["id"] = self.id
        d["width"] = self.width
        d["height"] = self.height
        d["x"] = self.x
        d["y"] = self.y
        return d
