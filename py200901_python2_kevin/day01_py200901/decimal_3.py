"""
round() - built-in function
round(target)
round(target, number of decimal places)
"""

from decimal import Decimal

# x = float(1)
x = Decimal(1)
print(x)

result = round(x,2)

print(result)

#
x = Decimal(1.256)
print(x)

result = round(x,2)

print(result)


#
x = Decimal(123.56)
result = round(x)
print(result)