"""
case:  using global variable in local scope
"""

def foo():
    global x
    print(x)
    x = x+1


x = 10
print(x)

foo()

print(x)

