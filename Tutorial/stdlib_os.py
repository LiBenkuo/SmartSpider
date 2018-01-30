# -*- coding: utf-8 -*-

# os module provides dozens of functions for interacting with the OS
import os

# shutil module provides a higher level interface that is easier to use
# for daily file and directory management tasks
import shutil

#----------------
# os module
#----------------
print(os.getcwd())       # Return current working dir

os.chdir('../')          # Change current working dir
print(os.getcwd())

os.system('ls')  # Run the command in the system shell

# return a list of all module functions
# print(dir(os))

# return an extensive manual page creatd from the module's docstrings
# print(help(os))

#----------------
# shutil module
#----------------
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('source', 'destination')

