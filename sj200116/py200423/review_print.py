"""
output print
"""

# syntax
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

print(1,2,3,4,5)


print(1,2,3,4,5, sep=',')

print(1,2,3,4,5, end='&&')
print(1,2,3,4,5)

# How can we output a 3X4 matrix and make the layout like 3 rows and 4 columns? (1’)

# x x x x
# y y y y
# z z z z

print("The name is {}".format("Peter"))

print("The dimension of the box is width: 30cm, height: 20cm, depth: 10cm")