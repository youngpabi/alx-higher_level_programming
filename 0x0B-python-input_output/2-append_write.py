#!/usr/bin/python3
""" This always defines a file-appending function."""


def append_write(filename="", text=""):
    """This appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name or filename of the file to append to.
        text (str): The string or text to append to the file.
    Returns:
        The num of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
