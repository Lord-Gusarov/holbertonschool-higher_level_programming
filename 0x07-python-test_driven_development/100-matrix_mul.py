#!/usr/bin/python3
"""This module multiplies 2 matrices
---(No modules may be impoerted)
"""


def matrix_mul(m_a, m_b):
    """Multiples 2 matrices, the arguments are cheked and
    exceptions raised if the input or they format in not adequate.
    Args:
        m_a ( [[]] of int, float): a matrix
        m_b ( [[]] of int, float): another matrix
    Returns:
        [[]] of int, floats: a new matrix of int and/or floats
    """

    dic = [("m_a", m_a), ("m_b", m_b)]
    """Wanted something similar to an ORDERED Python Dictionary to make sure
    'm_a' was always avaluated first"""

    for k, m in dic:
        if type(m) is not list:
            raise TypeError("{} must be a list".format(k))
    for k, m in dic:
        for x in m:
            if type(x) is not list:
                raise TypeError("{} must be a list of lists".format(k))
    for k, m in dic:
        if m == [] or m == [[]]:
            raise ValueError("{} can't be empty".format(k))
    for k, m in dic:
        for alist in m:
            if any(map(lambda x: type(x) not in [int, float], alist)):
                raise TypeError(("{} should contain only integers " +
                                "or floats").format(k))
    for k, m in dic:
        size = len(m[0])
        if any(map(lambda x: len(x) != size, m)):
            raise TypeError(("each row of {} must be of the same " +
                             "size").format(k))
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return [[sum(a*b for a, b in zip(ma_row, mb_col)) for mb_col
             in zip(*m_b)] for ma_row in m_a]
