"""
scope

type 1. global scope
type 2. local scope

global variable, global scope
In python, global variables declared outside of the function or in global scope is known
as global variables.


local variable, local scope


"""

def foo1():
    b = 1
    pass

def foo2():
    """
    you can access (read) global variable inside a function
    :return:
    """
    print("inside foo2() a = ",a)
    # print(b)
    pass

def foo3():
    """
    you cannot write (update) global variable inside a function
    :return:
    """
    # a = a + 1
    pass


a = 1
# print(b)
print("in global scope a =",a)
foo2()











