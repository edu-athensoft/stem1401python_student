"""
Recursion
is the process of defining something in terms of itself.

1. Getting image from mirror and reflects from each other infinitely
2. monthly payment


Recursive function
a function can call other functions (itself)
"""

x = 1
def foo(x):
    print("foo()", x)
    x = x + 1
    foo(x)

foo(1)
