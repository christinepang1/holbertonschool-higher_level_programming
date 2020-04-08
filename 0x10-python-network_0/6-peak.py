#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""
from math import floor


def find_peak(list_of_integers):
    """Finds a peak in a list"""
    if list_of_integers is None or list_of_integers == []:
        return None
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)

    return helper(list_of_integers, 0, len(list_of_integers) - 1)


def helper(li, start, end):
    """Updating the mid"""
    m = (end + start) // 2
    if (m == 0 or li[m - 1] <= li[m]) and (m ==
                                           len(li) - 1 or li[m] >= li[m + 1]):
        return li[m]
    elif m > 0 and li[m - 1] > li[m]:
        return helper(li, 0, m)
    else:
        return helper(li, m + 1, end)
