"""
local variables and local scope

"""

def foo1():
    # local variable
    x = 1
    print("x inside foo1() is ", x)


foo1()

# we cannot access local variables outside function or in global scope
# print("can i access x inside a function?", x)