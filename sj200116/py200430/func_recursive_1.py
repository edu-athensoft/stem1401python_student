"""
recursive function

fact: a function can call another function in itself

"""


def foo1():
    print("foo1()")


def foo2():
    print("foo2()")
    foo1()


foo1()
print()

foo2()
