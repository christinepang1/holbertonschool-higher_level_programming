#!/usr/bin/python3
for first in range(0, 9):
    for second in range(first + 1, 10):
        print("{}".format(first), end="")
        if first == 8 and second == 9:
            print("9", end="\n")
        else:
            print("{}".format(second), end=", ")
