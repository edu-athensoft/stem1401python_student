"""
lambda function / anonymous function
lambda expression
In Python, anonymous function is a function that is defined without a name.

1. simpler syntax
2. use only once, no need for name
3. pass a function as an argument, high order function
"""

def foo(x):
    return x

print(foo(1))


def foo2(f, x):
    return x


"""
lambda arguments: expression
lambda [arg1 [,arg2,.....argn]]:expression

keyword:  lambda
arguments
colon
expression
"""

def double(x):
    return 2 * x


# define a lambda function
dbl = lambda x: 2*x

# call
print(dbl(1))

db2 = lambda x: 2*x
print(db2(2))


# define a lambda function to calculate x-square  x^2
sqr = lambda x: x**2
sqr2 = lambda x: x*x

# parameter name can be any valid one
sqr = lambda a: a**2

# multiple argument(parameter)
# sum = n1 + n2
sum2 = lambda x,y : x+y

def sum2(x,y):
    return x+y

# return something
# one expression, no multiple statement










