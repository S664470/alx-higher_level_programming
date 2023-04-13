#!/usr/bin/python3
""" function that writes an Object to a text file"""


import json


def save_to_json_file(my_obj, filename):
    """
    ---
    my_obj - object to convert to a json formatted string
    ---
    filename text file
    """
    with open(filename, 'w') as fi:
        json.dump(my_obj, fi)
