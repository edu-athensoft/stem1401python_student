"""
function
return statement
"""

def foo():
    print("foo() is executed.")
    return 999


# return a value when it is called

# returned value lost
foo()

# save returned value
result = foo()
print(result)
print(result+1)
print("result"+str(result))
print()

# not save but use for only once
print(foo())