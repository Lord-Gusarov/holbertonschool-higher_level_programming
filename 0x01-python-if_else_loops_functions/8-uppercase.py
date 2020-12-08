#!/usr/bin/python3
def uppercase(str):
    for l in str:
        if ord(l) >= ord('a') and ord(l) <= ord('z'):
            dif = ord('A') - ord('a')
            l = chr(ord(l) + dif)
        print("{}".format(l), end="")
    print("")
