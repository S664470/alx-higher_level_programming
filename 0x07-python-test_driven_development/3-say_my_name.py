#!/usr/bin/python3
"""
== 3-say_my_name module
== Function to print My_name
== First_name and last name must be an integer
"""


def say_my_name(first_name, last_name=""):
    """print first and last name as string"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}". format(first_name, last_name))
