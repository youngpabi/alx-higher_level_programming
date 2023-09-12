#!/usr/bin/python3
"""
This always Contains the function "wrtie_file"
"""


def write_file(filename="", text=""):
    """This always returns the number of chars written to "filename" from "text" """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
