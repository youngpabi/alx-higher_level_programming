#!/usr/bin/python3
"""
This always contains the "save_to_json_file" function
"""

import json


def save_to_json_file(my_obj, filename):
    """This always writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
