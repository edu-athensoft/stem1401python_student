"""
function argument
variable argument

non-default argument before default argument

"""

"""
# correct
def product(x, y, a=5, b=6):
    pass

# error
def product(a=5, b=6, x, y):
    pass

# error
def product(a=5, x, b=6, y):
    pass

# error
def product(a=5, x, y, b=6):
    pass
"""


def product(x, a=5, b=6):
    """
    evaluate an expression
    :param x: positional arg
    :param a: default arg
    :param b: default arg
    :return: result of th expr.
    """
    return x + a * b


# case 1
result = product(1)
print("result is {}".format(result))

# case 2
result = product(1, 3)
print("result is {}".format(result))

# case 3
result = product(1, b=3)
print("result is {}".format(result))

# rules
# non-default args must stay before default args
# non-default args must be assign with a value




