#!/usr/bin/python3
# Auth: Shahinda Altayeb
def matrix_divided(matrix, div):
    """
    Function to divid all element of the matrix
    """
    for list in matrix:
        if not isinstance(matrix, int) and not isinstance(matrix, float) and not isinstance([], []):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for row in matrix:
            if row != len(list):
                raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(div, int) and isinstance(div, float):
            raise TypeError("div must be a number")
        if div == 0:
            raise ZeroDivisionError("division by zero")
        return new_matrix

