"""
string.format()

output using keyword arguments
"""

# output width, height and depth of a box

width = 10.0
height = 5.0
depth = 8.0

# print out the dimension of the box
strtemp = "The dimension of the box is: width={} inches, height={} inches, depth={} inches."
print(strtemp.format(width, height, depth))

strtemp = "The dimension of the box is: width={0} inches, height={1} inches, depth={2} inches."
print(strtemp.format(width, height, depth))
print()

strtemp = "The dimension of the box is: height={1} inches, width={0} inches, depth={2} inches."
print(strtemp.format(width, height, depth))

strtemp = "The dimension of the box is: depth={2} inches, height={1} inches, width={0} inches."
print(strtemp.format(width, height, depth))

# keyword argument
strtemp = "The dimension of the box is: width={width} inches, height={height} inches, depth={depth} inches."
print(strtemp.format(width=width, height=height, depth=depth))