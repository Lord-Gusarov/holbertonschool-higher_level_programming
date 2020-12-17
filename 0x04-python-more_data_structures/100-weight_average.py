#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1, sum2 = 0, 0
    for tp in my_list:
        v1, v2 = tp
        sum1 += v1 * v2
        sum2 += v2
    if sum2 == 0:
        return 0
    return sum1/sum2
