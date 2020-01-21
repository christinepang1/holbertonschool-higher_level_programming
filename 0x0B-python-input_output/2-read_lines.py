#!/usr/bin/python3
"""Function that reads n lines of a text file and prints to stdout"""


def read_lines(filename="", nb_lines=0):
    """Read lines of a text file"""
    lines = 0
    with open(filename, encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end="")
            return
        for i in f:
            if lines < nb_lines:
                print(i, end="")
            lines += 1
