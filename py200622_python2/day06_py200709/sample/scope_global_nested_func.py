"""

"""


def foo():
    x = 20

    def bar():
        global x
        x = 25

    print("Before calling bar: ", x)    # x is local variable in foo()

    print("Calling bar now")
    bar()
    print("After calling bar: ", x)     # x is local variable in foo()


x = 10
print("x in main : ", x)
print()

foo()
print()

print("x in main : ", x)
