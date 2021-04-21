"""
variables in the same name in both global and local scope
"""

def foo():
    x = 20
    x = x + 1
    print("local x = {} ".format(x))





x = 10
print("1. global x = {} ".format(x))

x = x + 1

foo()

print("2. global x = {} ".format(x))







