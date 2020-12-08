#!/usr/bin/python3
i = 0
dif = ord('A') - ord('a')
for l in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 1:
        print(chr(l + dif), end="")
    else:
        print(chr(l), end="")
    i += 1
