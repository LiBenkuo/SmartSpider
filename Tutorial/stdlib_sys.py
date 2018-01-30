# -*- coding: utf-8 -*-

import sys

print(sys.argv)

# `getopt` module processes sys.argv using the conventions of the Unix `getopt()` function
# More powerful and flexible command line processing on `argparse` module

# emit warnings and error messages to make them visible even when stdout has been redircted
sys.stderr.write('Warning, log file not found starting a new one\n')

# the most direct way to terminate a script
sys.exit()
