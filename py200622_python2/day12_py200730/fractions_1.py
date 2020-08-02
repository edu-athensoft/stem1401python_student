"""
fractions

mathematica
matlab

"""

import fractions
from fractions import Fraction as F

# 1.5
print(fractions.Fraction(1.5))

# 1/3
print(fractions.Fraction(1, 3))

# 5
print(fractions.Fraction(5))

# 5
print(fractions.Fraction(5, 1))

# 1.1 float number
print(fractions.Fraction(1.1))
print(2476979795053773/2251799813685248)

# 11/10
print(fractions.Fraction('1.1'))


# 1/3 + 1/3 = 2/3
result = F(1,3) + F(1,3)
print("1/3 + 1/3 = {}".format(result))

result = F(1,2) + F(1,3)
print("1/2 + 1/3 = {}".format(result))

result = 1/F(1,3)
print("1/F(1,3) = {}".format(result))

result = 1/F(3,1)
print("1/F(3,1) = {}".format(result))

result = 1/F(5,6)
print("1/F(5,6) = {}".format(result))

result = F(-3,10) > 0
print("F(-3,10) > 0 is {}".format(result))




