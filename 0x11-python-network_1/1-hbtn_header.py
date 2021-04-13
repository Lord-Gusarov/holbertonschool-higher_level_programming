#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the value of the
X-Request-Id variable found in the header of the response.
"""
from sys import argv
import urllib.request


with urllib.request.urlopen(argv[1]) as response:
    print(response.getheader('X-Request-Id'))
