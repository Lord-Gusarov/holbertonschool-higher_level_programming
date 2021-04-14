#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub
API to display your id
"""
from sys import argv
import requests


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user, passwd = argv[1:3]
    response = requests.get(url, auth=(user, passwd))
    r_dict = response.json()
    print(r_dict.get('id'))
