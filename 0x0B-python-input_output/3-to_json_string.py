#!/usr/bin/python3
"""
3-to_json_string
"""

import json

def to_json_string(my_obj):
    """returns the JSON representation of an object"""

    ret_str = json.dumps(my_obj)
    return ret_str
