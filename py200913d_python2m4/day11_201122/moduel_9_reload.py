"""
reload a group of statement
"""

import py200913d_python2m4.day11_201122.mymod3 as m3
# import py200913d_python2m4.day11_201122.mymod3 as m3       # ignored

print()
print("main program")
print()
print()

# reload

import importlib

importlib.reload(m3)
print()
print("main program 2")

