#!/usr/bin/python3
def roman_to_int(roman):
    if not isinstance(roman, str):
        return 0
    n = 0
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    l = len(roman) - 1
    while l >= 0:
        n += vals[roman[l]]
        while (l > 0 and vals[roman[l - 1]] < vals[roman[l]]):
            l -= 1
            n -= vals[roman[l]]
        l -= 1
    return n
