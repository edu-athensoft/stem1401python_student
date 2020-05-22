"""
explain lambda function
"""

import math


def foo(x):
    return 10 * math.sqrt(x)

print(foo(100))
print(foo(90))
print(foo(80))
print(foo(70))
print(foo(60))
print(foo(50))
print(foo(40))
print(foo(30))
print(foo(20))
print(foo(10))
print(foo(0))
print()

curve = lambda x : 10* math.sqrt(x)
print(curve(100))
print(curve(90))
print(curve(80))
print(curve(70))
print(curve(60))
