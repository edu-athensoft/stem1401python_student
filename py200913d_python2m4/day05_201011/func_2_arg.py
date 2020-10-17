"""
function argument

the number of parameter, argument
"""

# case 1.
def foo(x):
    return 2*x+1


# more than the one defined
# result = foo(1, 1, 2)


# case 2.
def foo2(w, v):
    return 2*w+v

result = foo2(2, 3)
print("result = ",result)

result2 = foo2(5)
print("result2 = ",result2)