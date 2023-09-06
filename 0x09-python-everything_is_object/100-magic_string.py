#!/usr/bin/python3
def magic_string():
    magic_string.count = 1 + getattr(magic_string, 'count', 0)
    return ", ".join(["BestSchool" for i in range(magic_string.count)])
