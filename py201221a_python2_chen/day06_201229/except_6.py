"""
try
except

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
try:
    f1()
except Exception:
    print("Waring: there is an exception!")

print("end")

print("continue to work")
