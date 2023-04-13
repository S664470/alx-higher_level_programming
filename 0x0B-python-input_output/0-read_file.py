#!/usr/bin/python3
"""Read UTF8"""


def read_file(filename=""):
    """opening file by with it take care of closing the file"""

    with open(filename, 'r', encoding='UTF8') as file:
        for line in file:
            print(line, end='')
