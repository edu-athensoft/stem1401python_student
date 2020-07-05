"""

"""


def foo(x):
    print("foo(x) is called and x is {}".format(x))


def foo2(x):
    global a
    a = a + 1
    print(a+1)
    return "foo2(x) is called and x is {}".format(x)

a = 10


# def foo3():
#     v1 = input("Please input a number:")
#     print(int(v1))

def foo3(v1):
    # v1 = input("Please input a number:")
    print(int(v1))


