"""
datatype decimal
"""

import decimal

print(0.1)

print(decimal.Decimal(0.1))
print(decimal.Decimal(0.1))
print(decimal.Decimal(0.1))

print(0.2)

print(decimal.Decimal(0.2))
print(decimal.Decimal(0.2))
print(decimal.Decimal(0.2))

print(0.3)

print(decimal.Decimal(0.3))
print(decimal.Decimal(0.3))
print(decimal.Decimal(0.3))
print()

a1 = decimal.Decimal(0.1)+decimal.Decimal(0.2)
a2 = 0.1+0.2
print(a1)
print(a2)

b1 = decimal.Decimal(0.3)
b2 = 0.3
print(b1)
print(b2)
print()

print(a1==b1)
print(a2==b2)




