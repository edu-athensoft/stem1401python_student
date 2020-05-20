"""
caller
"""

import py200421.day07_py200512.game.callee as callee

# method #1
callee.foo(1)


# method #2
print(callee.foo2(2))


# method 1
def input_kb():
    v1 = input("integer number value 1")
    return int(v1)

# function (arg1, [arg2, arg3])
callee.foo3(input_kb())

# method 2 - global variable
