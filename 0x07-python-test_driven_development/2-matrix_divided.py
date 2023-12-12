#!/usr/bin/python3
"""This module contains a function that divides all elements of a matrix

"""

def matrix_divided(matrix, div):
    """This function divides all elements of a matrix by a given number

    Args:
        matrix: A list of lists (matrix)- members can be of type ints or floats
        div: Number to be used for the division (can be a float or an integer)
    Raises:
          TypeError: If the matrix contains non-numbers
          TypeError: If the matrix contains rows of different sizes
          TypeError: If div is not an int or float
          ZeroDivisionError: If div is 0
    Returns:
           A new matrix which represents the result of the divisions
    """
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix
