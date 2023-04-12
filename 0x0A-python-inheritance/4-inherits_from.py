#!/usr/bin/python3
"""Return True or False"""


def inherits_from(obj, a_class):
    """isinstance to return an objevt of the class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
