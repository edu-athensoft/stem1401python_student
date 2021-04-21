"""
anonymous function
lambda function

lambda expression

high order function
lambda function can be taken as an argument and passed in a function
"""


"""
syntax
keyword:   lambda

lambda [arg1, [arg2, arg3, ...] : expression
"""


def foo(arg1, arg2, arg3):
    # expression
    pass

# high order function



def double(x):
    return 2*x


result = double(3)
print(f"Result is {result}")

# define a lambda function
double2 = lambda x : 2*x

result = double2(5)
print(f"Result of lambda is {result}")


f = double2
result = f(6)
print(f"Result of lambda is {result}")




