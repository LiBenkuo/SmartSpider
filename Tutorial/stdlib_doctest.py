# -*- coding: utf-8 -*-

# `doctest` module provides a tool for scanning a module and validating tests embedded in a program's docstrings

def average(values):
    """Computes the arithmetic mean of a list of numbers.
    >>> print(average([20, 30, 70]))
    50.0
    """
    return sum(values) / len(values)

import doctest

doctest.testmod()    # automatically validate the embedded tests
