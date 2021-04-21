"""
homework solution
"""

import random

res1 = []
for n in range(10000):
    res1.append(random.randrange(1,7))


# 6 containers
f1 = []
f2 = []
f3 = []
f4 = []
f5 = []
f6 = []

# iteration
for digit in res1:
    if digit == 1:
        f1.append(digit)
    if digit == 2:
        f2.append(digit)
    if digit == 3:
        f3.append(digit)
    if digit == 4:
        f4.append(digit)
    if digit == 5:
        f5.append(digit)
    if digit == 6:
        f6.append(digit)

# counting
num1 = len(f1)
print(1, num1/10000)

num2 = len(f2)
print(2, num2/10000)

num3 = len(f3)
print(3, num3/10000)

num4 = len(f4)
print(4, num4/10000)

num5 = len(f5)
print(5, num5/10000)

num6 = len(f6)
print(6, num6/10000)

print(1/6)