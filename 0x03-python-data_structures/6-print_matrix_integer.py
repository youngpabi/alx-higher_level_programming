#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mt in matrix:
        print(" ".join("{:d}".format(g) for g in mt))
