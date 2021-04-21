"""
local scope

local variable
"""

def foo():
    y = "local"
    print("inside foo() y is ",y)


foo()

# NameError: name 'y' is not defined
print(y)
