#!/usr/bin/python3
"""Read text file and print to stdout"""


def read_file(filename=""):
    """Reads file"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
