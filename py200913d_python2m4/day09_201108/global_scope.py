"""
global scope

global variable - A variable which is defined and takes effect in global scope
"""

x = "global3"

def foo():
    print("x inside:", x)


foo()
print("x outside:", x)