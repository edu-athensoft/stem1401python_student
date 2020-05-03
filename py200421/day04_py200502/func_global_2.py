"""
global variable, local variable

local scope
global scope

"""

def foo():
    print("in foo(), a = {}".format(a))

a = 1
foo()

print("========================")

def foo2():
    print("in foo2(), b = {}".format(b+1))

b = 1
foo2()

print("========================")

# def foo3():
#     c = c+1
#     print("in foo3(), c = {}".format(c))
#
# c = 1
# foo3()

# c = c+1
# print(c)
























