#!/usr/bin/python3
"""class myclass"""

class MyList(list):
    """class to print sorted list of an integer"""

    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

