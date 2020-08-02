"""
Module a file containing python statement and definitions

- global variables (definition)
- constants (definition)
- function (definition)
- class (definition)


module is python file.
"""

import py200622_python2.day10_200723.mymodule as mymodule

from py200622_python2.day10_200723.mymodule import foo3
# from py200622_python2.day10_200723.mymodule import foo1,foo2

# foo3()

# foo1()
# foo2()


# import math
# print(math.pi)
#
# from math import pi
# print(pi)

from math import *
print(pi)
print(abs(-100))


import sys
print(sys.path)

for path in sys.path:
    print(path)


# list all contents(names) in a module
items = dir(mymodule)

for item in items:
    print(item)



