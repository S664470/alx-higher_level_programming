#!/usr/bin/python3
"""Writting string to a text file with UTF8 and return number of char written"""


def write_file(filename="", text=""):
    """The process"""

    num_char_written = 0
    with open(filename, 'w', encoding='UTF8') as file:
        """w+ mode to create file if it doesn't exist"""

        num_char_written = file.write(text)
    return num_char_written
        
