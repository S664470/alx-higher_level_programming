#!/usr/bin/python3
"""Writting string to a text file with UTF8 and return number of char written"""


def write_file(filename="", text=""):
    """The process"""

    with open(filename, 'w', encoding='utf-8') as file:
        """w+ mode to create file if it doesn't exist"""

        num_char_written = file.write(text)
    return len(text)
