"""
piecewise function

input section for x

processing

output result
"""

# input section
# input from keyboard

x = input("please input x")
# x = 7
x = float(x)

# processing
y = 'unknown'
if x > 1:
    y = 3*x + 5
elif x >= -1:
    y = x+2
else:
    y = 5*x + 3

# output y aka f(x)
print("The result of y is {y_value} when x is {x_value}".format(x_value=x, y_value=y))


