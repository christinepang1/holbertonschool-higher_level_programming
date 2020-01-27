#!/usr/bin/python3
"""Base Class"""


import json


class Base:
    """Base Class"""

    __nb_objects = 0
    # private class attribute

    def __init__(self, id=None):
        """init base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representastion of list_objs to a file"""
        lo = []
        if list_objs is None:
            lo = []
        else:
            for i in list_objs:
                lo.append(i.to_dictionary())
        with open("{}.json".format(cls.__name__), mode="w") as f:
            f.write(Base.to_json_string(lo))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of JSON string representation json_string"""
        l = []
        if json_string is None or len(json_string) == 0:
            return l
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        if cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new
