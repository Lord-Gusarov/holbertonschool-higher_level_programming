#!/usr/bin/python3
def remove_char_at(str, n):
    nStr = ""
    for i in range(0, len(str)):
        if i != n:
            nStr = nStr + str[i]
    return (nStr)
