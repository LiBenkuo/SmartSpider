# -*- coding: utf-8 -*-

# `re` module provides regular expression tools for advanced string processing
import re

print(re.findall(r'\bf[a-z]*', 'which foot or head fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
