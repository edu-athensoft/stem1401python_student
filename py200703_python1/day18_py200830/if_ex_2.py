"""
ex 2.
write a program to find the largest number among 3 given numbers
"""

a = 24
b = 15
c = 6
d = 78

max = a

# 1st round
if max < a:
    max = a

# 2nd round
if max < b:
    max = b

# 3rd round
if max < c:
    max = c

# 4th round
if max < d:
    max = d

print("The max number is {}".format(max))

