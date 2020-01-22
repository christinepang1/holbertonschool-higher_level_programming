#!/usr/bin/python3
"""Class Student"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Init Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns dictionary description of self"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a student instance"""
        if not isinstance(attrs, list):
            return self.__dict__
        if attrs is None:
            return self.__dict__
        dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dict[i] = self.__dict__[i]
        return dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        keys = list(json.keys())
        for i in keys:
            if i in self.__dict__.keys():
                setattr(self, i, json[i])
