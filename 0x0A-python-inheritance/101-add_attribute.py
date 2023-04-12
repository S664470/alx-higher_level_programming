#!/usr/bin/python3
"""Afunctoin that add new attribute to an object"""

def add_attribute(obj, attr_name, attr_value):
    if hasattr(obj, attr_name):

        return False
    else:
        setattr(obj, attr_name, attr_value)
        return True
