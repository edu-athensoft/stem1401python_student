"""
return multiple values
"""

def foo(a, b):
    return a+1, b+1


def foo1(a, b):
    res1 = a+1
    res2 = b+1
    return res1, res2

# call a function
foo(1, 2)

print(foo(1,2))


# how to save returned values and print them out?
# 2,3 => 2 variables
x, y = foo(1, 2)
print("x = {}".format(x))
print("y = {}".format(y))

# x, y = 2, 3

