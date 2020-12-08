#!/usr/bin/python3
for i in range(0, 10):
    for ii in range(i + 1, 10):
        print("{:d}{:d}".format(i, ii), end="")
        if i * 10 + ii != 89:
            print(", ", end="")

print("")
