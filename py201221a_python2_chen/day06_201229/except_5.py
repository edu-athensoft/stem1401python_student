"""
handling exceptions

syntax errors
logical errors (exceptions)

keywords:

try
except (exception)
else
finally
"""


def f1():
    print("f1()")
    f2()


def f2():
    print("f2()")
    f3()


def f3():
    print("f3()")
    raise Exception


# main program
print("start")
f1()
print("end")






