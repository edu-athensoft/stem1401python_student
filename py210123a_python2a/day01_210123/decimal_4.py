"""
round(num, pre)
"""

from decimal import Decimal

# x = float(1)
x = Decimal(1)
print(x)

result = round(x,2)
result = round(x,4)

print(result)

x = Decimal(1.366)
print(x)

result = round(x,2)


print(result)
