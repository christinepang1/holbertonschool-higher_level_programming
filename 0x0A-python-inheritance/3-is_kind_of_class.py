#!/usr/bin/python3
"""
Checks if the object is an instance of, or if the object is an instance of a \
class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if is an instance in the same class, otherwise false"""
    return isinstance(obj, a_class)
