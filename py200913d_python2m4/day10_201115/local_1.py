"""
local variables are invisible in global scope
"""

def foo():
    a = 1
    print("a inside is {}".format(a))


print("a = {}".format(a))