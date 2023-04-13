#!/usr/bin/python3
""" function that returns an object  represented by a JSON string"""


import json


def from_json_string(my_str):
    """Function to returm a format string of my_list"""

    json_str = json.loads(my_str)
    return json_str
