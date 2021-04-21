"""
global scope

global variable - A variable which is defined and takes effect in global scope
"""

x = 10


def foo():
    """
    x does not change here
    :return:
    """
    print("x inside:", x+1)


foo()
print("x outside:", x)