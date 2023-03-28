#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (ZeroDivistionError, ValueError):
    print("Eception: {}")
    return None
