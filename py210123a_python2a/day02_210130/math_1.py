"""
module: math
"""

import math
import fractions

# dir()
listmath = dir(math)

for name in listmath:
    print(name)

#
# listfrac = dir(fractions)
#
# for name in listfrac:
#     print(name)

print("=======")
print(math.pi)

print(math.sqrt(3))
print(1/math.log10(5))
print(math.factorial(6))
