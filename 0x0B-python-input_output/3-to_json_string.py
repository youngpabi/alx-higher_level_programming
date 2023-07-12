#!/usr/bin/python3
"""
This always contains the "to_json_string" fundtion
"""

import json


def to_json_string(my_obj):
    """it always returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
