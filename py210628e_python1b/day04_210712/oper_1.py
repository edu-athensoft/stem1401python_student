"""
operator

An operator may be used in other way due to the data type of its operands.

"""


# expr = 3 + '5' * 2

# print(expr)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


expr2 = 3 + 2 * '5'
print(expr2)

# TypeError: unsupported operand type(s) for +: 'int' and 'str'



