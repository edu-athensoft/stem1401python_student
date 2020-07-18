"""
global and local variable and scope
"""

def foo():
    print(x)


def foo2():
    print(x+str(1))


# def foo3():
#     x = x + str(1)
#     print(x)


x = "global"
foo()
foo2()
# foo3()





