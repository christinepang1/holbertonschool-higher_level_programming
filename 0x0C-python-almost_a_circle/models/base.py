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
