#!/usr/bin/python3
"""Another way to Multiply 2 Matrixes
This module uses NumPy for Matrix multiplication
"""


def lazy_matrix_mul(m_a, m_b):
    """"Matrxi multiplication using NumPy
    Args:
        m_a: a matrix of integers or floats
        m_b: a matrix of integers or floats
    Returns:
        [[]]: matrix of the product of m_a with m_b
    """
    import numpy as np
    return np.matmul(m_a, m_b)
