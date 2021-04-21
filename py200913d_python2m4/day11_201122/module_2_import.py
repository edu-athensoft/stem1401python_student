"""
Why do we need to specify module names when importing them?
"""

import py200913d_python2m4.day11_201122.mymod1 as m1
import py200913d_python2m4.day11_201122.mymod2 as m2

x = 5
y = 4

# using mymod1
result1 = m1.foo(x, y)
print("The result is {}".format(result1))

# using mymod2
result2 = m2.foo(x, y)
print("The result is {}".format(result2))

