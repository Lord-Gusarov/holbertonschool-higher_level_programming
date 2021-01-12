#!/usr/bin/python3
"""This module defines a class whose attribute count can't be modified by
its user
"""


class LockedClass:
    __slots__ = ['first_name']
