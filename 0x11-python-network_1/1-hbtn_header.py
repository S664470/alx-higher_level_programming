#!/usr/bin/python3
"""Desplay the value of the X-Request-Id"""
import urllib.request
import sys


"""Get the url from the command line"""
url = sys.argv[1]

"""Send the request to get the response"""
with urllib.request.urlopen(url) as response:
    """Getting the value of the X-Request-Id"""
    header = response.getheader('X-Request-Id')
    """Value displaying"""
    print(header)
