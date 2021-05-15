"""
String formatting

returns a new string

"""

width = 20
height = 30
depth = 40


# case 1.
result = 'The dimension of the box is like width: {}, height: {}, depth: {}'.format(width, height, depth)
print(result)

# case 2.
result = 'The dimension of the box is like height: {1}, depth: {2}, width: {0}'.format(width, height, depth)
print(result)

# case 3.
result = 'The dimension of the box is like depth: {d}, width: {w}, height: {h}'.format(w=width,h=height,d=depth)
print(result)



