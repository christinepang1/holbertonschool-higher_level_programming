#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""
from math import floor


def find_peak(list_of_integers):
    """Finds a peak in a list"""
    if list_of_integers is None:
        return None

    #  if array is size of 1 or 2

    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)

    start = 0
    end = n - 1

    while (start <= end):
        m = (end + start) // 2
        if (m == 0 or list_of_integers[m - 1] <= list_of_integers[m]) and (
                m == n - 1 or list_of_integers[m] >= list_of_integers[m + 1]):
            return list_of_integers[m]
        elif m > 0 and list_of_integers[m - 1] > list_of_integers[m]:
            end = m - 1
        else:
            start = m + 1
