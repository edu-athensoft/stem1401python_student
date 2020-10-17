"""
function argument

positional arguments

"""


def foo():
    print("no param")


def foo2(n):
    return 2*n + 1


def foo3(a,b):
    return a*b


# match
# TypeError: foo() takes 0 positional arguments but 1 was given
# foo(1)

# res2 = foo2(3)
# print(res2)

# TypeError: foo2() missing 1 required positional argument: 'n'
# res2 = foo2()
# print(res2)

# TypeError: foo2() takes 1 positional argument but 2 were given
# res2 = foo2(1,2)
# print(res2)


res3 = foo3(2,3)
print(res3)

# res3 = foo3(2)
# print(res3)