"""
keyword
"""


"""
True, False, None
and, or, not
if, else, elif, for, while, break, continue
def, return, yield, lambda, pass
class
try, except,raise, finally, with
global, nonlocal
import, from, as
assert, del, in, is
"""

# valid name(identifier)
# rule 1: a-zA-Z0-9_
car = 'BMW'
CAR = 'Benz'
_car = 'Dodge'
c001 = 123
a_123 = 345
_123 = 456

# rule 2
# 0abc = 1

# rule 3
this_is_a_long_variable_name = 123

# rule 4
# !@#$%^&*()-+=[]{}\|

# &abc = 124
# abc& = 'abc'
# a&b = True

def foo(x):
    """
    this is a docstring for the function foo(x)
    :param x:
    :return:
    """
    print(x)

print(foo.__doc__)
























"""
case sensitive?
car
Car
CAR
cAR
cAr



case insenstive?
car
Car
CAR
cAR
cAr
"""




