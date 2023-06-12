#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = my_list.copy()

    if len(my_list) <= idx or idx < 0:
        return new

    new[idx] = element
    return new
