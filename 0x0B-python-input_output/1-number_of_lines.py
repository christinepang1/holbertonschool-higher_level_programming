#!/usr/bin/python3
"""Return number of lines in a text file"""


def number_of_lines(filename=""):
    """return number of lines in file"""
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for i in f:
            lines += 1
    return lines
