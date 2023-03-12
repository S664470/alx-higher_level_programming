#!/usr/bin/env python3
def no_c(my_string):
    noC = " "
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            noC += ch
    return (noC)
