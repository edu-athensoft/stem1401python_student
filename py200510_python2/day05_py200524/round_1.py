"""
round
"""

from decimal import Decimal

# x = float(1)
x = Decimal(1)

result = round(x,2)

print(result)

x = 9.4999
result = round(x)
print(result)

x = 9.4999
result = round(x,1)
print(result)

x = 9.4999
result = round(x,2)
print(result)
