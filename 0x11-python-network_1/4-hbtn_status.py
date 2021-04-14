#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status using the 'requests' package
"""
import requests


if __name__ == '__main__':
    response = requests.get('https://intranet.hbtn.io/status')
    content = response.content.decode('utf8)')
    out = "Body response:\n\t- type: {}\n\t- content: {}"
    print(out.format(type(content), content))
