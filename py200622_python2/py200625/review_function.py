"""


"""

# define a function
def foo1():
    print("1111")
    print("1112")
    print("1113")
    print("1114")
    print("1115")
    a = 1
    b = a+1
    print(b)
    return b


# call a function
print("=== the 1st call ===")
foo1()
print()

# get the returned value and just use it for only once
print("=== the 2nd call ===")
print(foo1())
print()

# get the returned value and use it for multiple times
print("=== the 3rd call ===")
# 1. print out (use) the returned value for the 1st time
result1 = foo1()
print("result = ",result1)
# 2. use the returned value again
doubled_result1 = 2 * result1
print("doubled_result1 = ",doubled_result1)



# call for multiple times
foo1()
foo1()
print(foo1())





