"""
lambda can accept more than one arguments
"""

# z = f(x, y)
# z = x + y

z = lambda x, y : x + y

# use lambda z
result = z(1,2)
print(result)



def z(x, y):
    # print("x={}, y={}".format(x,y))
    return x + y

