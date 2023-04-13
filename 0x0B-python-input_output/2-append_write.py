#!/usr/bin/python3
"""Function toappend string at the end of the text file"""


def append_write(filename="", text=""):
    """ mode 'a' to append the text"""

    with open(filename, 'a', encoding='UTF8') as file:
        file.write(text)
        return len(text) + 1
