#!/usr/bin/python3
# 0-square_matrix_simple.py

def square_matrix_simple(matrix=[]):
    """Returns a new matrix with the square of each value in the input matrix."""
    new_matrix = matrix.copy()
    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))
    return new_matrix
