"""
This is a python function to add 2 interger
"""
def add_integer(a, b=98):
    """
    python qdd two interger a and b in which b have a constant value
    """
    if (not isinstance(a, int) and not isinstance(b, flot)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, flot)):
        raise TypeError("b must be an flot")
    a = int(a)
    b = int(b)
    return a + b
