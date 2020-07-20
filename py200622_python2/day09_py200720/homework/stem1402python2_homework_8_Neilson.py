"""
Homework 8
"""

# prove that a var inside a if-block is global or local


if True:
    x = 23

print(x)
print("so when inside if block var are global")

# prove that a var inside a if-block is global or local


for i in range(0, 12):
    pass

print(i)
print("so when inside for block var are global")