"""
create 2 functions
1. y = 2x
2. y = 2x + 1
(whereas 2x mean 2 * x)
call each function for 3 time with different input x of x (value of x)
then print out the returned value of y
"""

# define function with the keyword 'def'
# define a function
def myfuc1(x):
    return x

# 1. y = 2x
# call a function
result = myfuc1(5) * 2
print("the result of myfuc1(5) is {} ".format(result))

# call a function again
result = myfuc1(10) * 2
print("the result of myfuc1(10) is {} ".format(result))

# call a function again
result = myfuc1(55) * 2
print("the result of myfuc1(55) is {} ".format(result))


# 2. y = 2x + 1
# call a function
result = myfuc1(5) * 2 + 1
print("the result of myfuc1(5) is {} ".format(result))

# call a function again
result = myfuc1(10) * 2 + 1
print("the result of myfuc1(10) is {} ".format(result))

# call a function again
result = myfuc1(55) * 2 + 1
print("the result of myfuc1(55) is {} ".format(result))