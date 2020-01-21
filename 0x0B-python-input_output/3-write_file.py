#!/usr/bin/python3
"""Writes a string to a text file and returns number of characters written"""


def write_file(filename="", text=""):
    """Writes text to filename"""
    with open(filename, mode='w', encoding='utf-8') as f:
        my_file = f.write(text)
    return my_file
