# -*- coding: utf-8 -*-

# `random` module provides tools for making random selections
import random

print(random.choice(['apple', 'banana', 'pear']))

# sampling without replacement
print(random.sample(range(100), 10))

# random float
print(random.random())

# random integer chosen from range(6)
print(random.randrange(6))
