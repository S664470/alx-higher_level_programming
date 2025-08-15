#!/usr/bin/python3
"""
Funiction compute addition of two number

The two must be integer or float
"""
def add_integer(a, b=98):
    """
    Raise : TypeError if a or be are not an integer ofr float
    """


    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)

    return (a + b)
