#!/usr/bin/python3
def magic_string(cnt=[0]):
    cnt[0] += 1
    return "Holberton, " * (cnt[0] - 1) + "Holberton"
