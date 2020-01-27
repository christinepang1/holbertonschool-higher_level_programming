#!/usr/bin/python3
"""Square Class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading __str___ method should return syntax"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if kwargs is not None and len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
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
                self.size = args[1]
                return
            if len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                return
            if len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
                return
