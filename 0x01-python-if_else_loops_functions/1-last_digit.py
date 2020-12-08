#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 1:
    digit = ((number * -1) % 10) * -1
else:
    digit = number % 10

if digit > 5:
    desc = "greater than 5"
elif digit == 0:
    desc = "0"
else:
    desc = "less than 6 and not 0"

print("Last digit of {:d} is {:d} and is {:s}".format(number, digit, desc))
