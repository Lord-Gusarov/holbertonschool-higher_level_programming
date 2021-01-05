#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum = [0, 0]
    for i in range(0, 2):
        try:
            sum[i] += tuple_a[i]
        except:
            sum[i] += 0
        try:
            sum[i] += tuple_b[i]
        except:
            sum[i] += 0
    tsum = tuple(sum)
    return tsum
