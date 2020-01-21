#!/usr/bin/python3
"""Inherited list class Mylist"""


class MyList(list):
    """
    List
    """
    def print_sorted(self):
        """
        Sorts list and prints it
        """
        print(sorted(self))
