"""
lambda can accept more than one arguments
"""

# y = x^2 + 2*x + 1
# x = 5, y=?

y = lambda a : a**2 + 2*a + 1

x = 5
result = y(x)
print(result)



# z = x^2 + 2*x*y + y^2
# test x = 5, y = 3,  z =?

z = lambda x,y: x**2 + 2*x*y + y**2

x = 5
y = 3
result = z(x, y)
print(result)

