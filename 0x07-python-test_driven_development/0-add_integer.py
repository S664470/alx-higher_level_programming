#!/usr/bin/python3
# Auth: Shahinda Altayeb

def add_integer(a, b=98):
    """
    Function:
    add 2 integer
    variable:
    a and b must be integer or floats other wise must be an error
    THE 2 number must be casted to int if they are float
    Return:
    an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return a + b
