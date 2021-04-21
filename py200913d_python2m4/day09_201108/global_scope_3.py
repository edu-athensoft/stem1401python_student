"""
global scope

global variable - A variable which is defined and takes effect in global scope

Global variables are read-only within functions

"""

x = 10


def foo():
    """
    x can not be changed here
    :return:
    """
    # x = x + 1
    x = x
    print("x inside:", x)


foo()
print("x outside:", x)