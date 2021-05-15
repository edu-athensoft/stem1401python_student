"""
fraction

f = p/q   (p, q are integers, q!=0)

A fraction has a numerator and a denominator,
both of which are integers.
This module has support for rational number arithmetic.
"""

import fractions
from fractions import Fraction as F

f1 = fractions.Fraction(1.5)
print(f1)

f2 = fractions.Fraction(1.3)
print(f2)

f3 = fractions.Fraction('1.3')
print(f3)


f4 = F(1.6)
print(f4)

f4 = F('1.6')
print(f4)


# accepting 2 parameters
f5 = F(8,3)
print(f5)

f6 = F(1,5)
print(f6)

