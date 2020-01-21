#!/usr/bin/python3
"""Appends string to end of a text file and returns number of char added"""


def append_write(filename="", text=""):
    """Appends text to filename"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
