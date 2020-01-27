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
