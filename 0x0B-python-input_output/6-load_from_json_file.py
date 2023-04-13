#!/usr/bin/python3
"""
Creat AN Obiect from “JSON file”
"""


import json


def load_from_json_file(filename):
    """
    open the file for reding
    ---
    load the jason data
    """

    with open(filename, 'r') as f:
        obj = json.load(f)
        return obj
