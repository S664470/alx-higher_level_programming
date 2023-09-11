#!/usr/bin/python3
"""
contain list of class

"""


class MyList(list):
    """class that inherat from another"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
