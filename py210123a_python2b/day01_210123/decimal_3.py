"""
decimal and precision
"""

from decimal import Decimal as D

print(D(1.1)+D(2.2))
print(D(3.3))

res = D('1.1') + D('2.2')
print(type(res))

print(res)


print(res == D('3.3'))


res = D('1.2') * D('2.50')
print(res)

res = D('1.2') * D('2.5')
print(res)

res = D('1.2') * D('2.500')
print(res)


print(1.2*2.5)
print(1.2*2.50)
print(1.2*2.500)
