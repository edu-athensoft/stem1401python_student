"""
Recursion is the process of defining something in terms of itself.

"""


def foo1():
    print("foo1() is called.")


def foo2():
    print("foo2() is called.")
    foo1()


foo1()
print()

foo2()





