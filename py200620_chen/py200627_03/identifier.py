"""
python identifier

An identifier is a name

python entities:
    variable
    constant
    function
    class
    ...
"""

# rules for identifiers
# 1. valid chars:  a-zA-Z0-9_
# 2. a-zA-Z_
# 3. of any length
# 4. not to use keywords and reserved words


# special identifiers

# __doc__

def foo1(x):
    """
    description of foo1
    :param x: the input value
    :return:  doubled value of the input
    """
    return 2*x

print(foo1.__doc__)


# coding convention for identifiers
thisisalongname = 56
this_is_a_long_name = 56

# case-sensitive
Car = "BMW"
car = "bmw"
# cAR != car
# CAR != caR

# 
number_of_student = 25
nos = 25








