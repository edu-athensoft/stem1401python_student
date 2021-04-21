"""
operate on global variable in local scope

keyword:  global
"""

x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(y)
    print(x)

print("before ")
print(x)
print()

print("after")
foo()
print()

print(x)


