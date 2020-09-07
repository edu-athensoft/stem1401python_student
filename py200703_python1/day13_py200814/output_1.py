"""
output format()
output formatting with placeholders

string.format()

string template
placeholder
"""

x = 1 + 3*4
y = 2 + 5*6

# not recommended
print('x=', x, ',', 'y=', y)

# recommended
print("x={} , y={}")
print("x={} , y={}".format(x, y))
print("x={},y={}".format(x, y))
print("x={}, y={}".format(x, y))
