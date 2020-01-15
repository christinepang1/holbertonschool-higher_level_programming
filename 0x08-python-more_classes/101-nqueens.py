#!/usr/bin/python3
import sys

"""N Queens"""


class nQueens:

    def __init__(self, n):
        """Initialize by size of board"""
        self.n = n

    @property
    def n(self):
        """Getter for n"""
        return self.__n

    @n.setter
    def n(self, value):
        """Setter for n"""
        if value < 4:
            print("N must be at least 4")
            exit(1)
        self.__n = value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    nQueens = nQueens(n)
