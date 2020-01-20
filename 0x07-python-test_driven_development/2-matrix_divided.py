#!/usr/bin/python3
"""
Divide a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Iterate through a matrix and divide by div
    """
    te = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(te)
    for x in matrix:
        if not isinstance(x, list):
            raise TypeError(te)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    for x in matrix:
        for n in x:
            if not isinstance(n, (int, float)):
                raise TypeError(te)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(te)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    new = []
    for row in matrix:
        new.append([round((n/div), 2) for n in row])
    return new
