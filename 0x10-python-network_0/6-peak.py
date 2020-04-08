#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""
from math import floor


def find_peak(list_of_integers):
    """Finds a peak in a list"""
    if list_of_integers is None:
        return None

    #  if array is size of 1 or 2

    size = len(list_of_integers)
    start = 0
    end = size - 1

    while (start <= end):
        mid = (end + start) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and (
                mid == size - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            end = mid - 1
        else:
            start = mid + 1
