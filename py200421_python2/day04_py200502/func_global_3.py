"""
global scope and global variable

keyword: global
"""

def foo():
    global a
    a = a + 1
    print("local scope,  a = {}".format(a))



a = 10
print("global scope 1, a = {}".format(a))

foo()
print("global scope 2, a = {}".format(a))