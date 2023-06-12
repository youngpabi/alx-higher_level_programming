#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_xt = min(my_list)
    for n in my_list:
        if n > max_xt:
            max_xt = n

    return max_xt
