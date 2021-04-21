"""
scope best practice
"""


"""
# this function depends on global variable of x
# using 'global' keyword
x = 10

def foo():
    global x
    x = x + 1
    return x

print(foo())
"""


# this function has nothing to do with global variable of a
# using arguments
def foo(abc):
    abc = abc + 1
    return abc

a = 10
print(foo(a))



