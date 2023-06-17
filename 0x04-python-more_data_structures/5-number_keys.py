#!/usr/bin/python3
def number_keys(a_dictionary):
    nums = 0
    list_keys = list(a_dictionary.keys())
    for n in list_keys:
        nums += 1

    return (nums)
