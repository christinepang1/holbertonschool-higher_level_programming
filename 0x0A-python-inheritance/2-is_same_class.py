#!/usr/bin/python3
"""Function that checks if object is in the class"""


def is_same_class(obj, a_class):
    """Returns true if bject is in the same class"""
    if type(obj) == a_class:
        return True
    return False
