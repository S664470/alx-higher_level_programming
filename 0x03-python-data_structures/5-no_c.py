#!/usr/bin/env python3
def no_c(my_string):
        for ch in range(my_string):
            if ch != 'c' and ch != 'C':
                return(ch)
