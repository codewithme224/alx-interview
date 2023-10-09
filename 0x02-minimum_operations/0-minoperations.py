#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """[summary]

    Args:
        n ([type]): [description]

    Returns:
        [type]: [description]
    """
    if n < 2:
        return 0
    operations = 0
    i = 2
    while i <= n:
        if n % i == 0:
            operations += i
            n = n / i
        else:
            i += 1
    return operations
