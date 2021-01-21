#!/usr/bin/python3
"""Pascal Triangle
"""


def pascal_triangle(n):
    """Return an (n) len Pascal triangle
    """
    if n < 1:
        return []
    r = []
    l = [1]
    for i in range(n):
        r.append(l)
        m = l[:] + [0]
        idx = 1
        for x in l:
            m[idx] += x
            idx += 1
        l = m
    return r
