#!/usr/bin/python3
"""Function that adds two integers"""


def add_integer(a, b=98):
    """Adds two integers together"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    a = int(a)
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    b = int(b)
    return a + b
