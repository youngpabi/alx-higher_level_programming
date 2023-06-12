#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    A, B = len(tuple_a), len(tuple_b)
    n_tuple = ((tuple_a[0] if A >= 1 else 0) + (tuple_b[0] if B >= 1 else 0),
                 (tuple_a[1] if A >= 2 else 0) + (tuple_b[1] if B >= 2 else 0))
    return n_tuple
