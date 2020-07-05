"""

"""

from fractions import Fraction as F

# 1/3 + 1/3 = 2/3
result = F(1,3) + F(1,3)
print("1/3 + 1/3 = {}".format(result))

result = 1/F(1,3)
print("1/F(1,3) = {}".format(result))

result = 1/F(5,6)
print("1/F(5,6) = {}".format(result))

result = F(-3,10) > 0
print("F(-3,10) > 0 is {}".format(result))

