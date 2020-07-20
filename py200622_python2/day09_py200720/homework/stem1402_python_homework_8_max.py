"""
Homework 8 max
"""

# if-block
if 1 == 1:
    x = 123

print("global x =", x)

if x == 123:
    print("x is a global variable")

else:
    print("x is not a global variable")

# for-block
for i in (1,2,3):
    pass

if i == 3:
    print("i is a global variable")

else:
    print("i is not a global variable")
