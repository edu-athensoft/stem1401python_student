"""
decimal module

"""

# import decimal
from decimal import Decimal

print(Decimal(1.1))
print(Decimal(2.2))
print(Decimal(3.3))

print()

print(Decimal('1.1'))
print(Decimal('2.2'))

result = Decimal('1.1') + Decimal('2.2')
print(result, type(result))

result = Decimal('1.1') - Decimal('2.2')
print(result, type(result))

result = Decimal('1.2') * Decimal('2.5')
print(result, type(result))

result = Decimal('1.2') * Decimal('2.50')
print(result, type(result))

res = Decimal('1.2') * Decimal('2.500')
print(res)

# a = Decimal('1.1')
# b = Decimal('2.2')
# c = Decimal('3.3')
#`````````````````
# if a + b == c:
#     print("yes")

# usd to cad
# usd $1000000 TO ? CAD





