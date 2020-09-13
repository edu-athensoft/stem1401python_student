"""
function argument
variable argument

default argument
non-default argument
"""


def product(a=5, b=6):
    return a * b


# case 1
result = product()
print("result is {}".format(result))


# case 2
result = product(3)
print("result is {}".format(result))


# case 3
result = product(3, 4)
print("result is {}".format(result))


# case 4
result = product(b=2)
print("result is {}".format(result))

# v.s.
# string format()





