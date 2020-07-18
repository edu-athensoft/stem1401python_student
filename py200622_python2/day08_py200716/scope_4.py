"""
scope 4.  nested function

global, nonlocal
"""


def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:",x)

    inner()
    print("outer:",x)


outer()
