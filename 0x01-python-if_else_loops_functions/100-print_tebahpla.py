#!/usr/bin/python3
i = 0
dif = ord('A') - ord('a')
for l in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 1:
        print("{}".format(chr(l + dif)), end="")
    else:
        print("{}".format(chr(l)), end="")
    i += 1
