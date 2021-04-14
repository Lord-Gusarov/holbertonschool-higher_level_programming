#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    out = q = ""
    if len(argv) > 1:
        q = argv[1]
    response = requests.post(url, data={'q': q})

    try:
        r_dict = response.json()
        if len(r_dict) == 0:
            out = "No result"
        else:
            out = "[{}] {}".format(r_dict.get('id'), r_dict.get('name'))
    except:
        out = "Not a valid JSON"
    print(out)
