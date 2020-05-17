"""
lambda function, anonymous function
"""

# regular function
def foo(x):
    print("foo({})".format(x))

foo(123)


# lambda
# arg1, [arg2, arg3,...]   accepting 1..n argument(s)
# one or short expression(arg1,[arg2, ...])

# syntax
# lambda arg1, [arg2, arg3,...]  : expr

# double a given number
# print out the result for users


def double(x):
    return 2*x

n = 1
print(double(n))


mydouble = lambda x: 2*x
m = 3
print(mydouble(m))