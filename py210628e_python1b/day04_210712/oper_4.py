"""
Assignment operators

assignment expression : from right to left

symbol:   =

compared with ==


"""

a = 100

x = y = z = 6

# z = 6
# y = 6
# x = 6


# Compound operator
# 1. arithmetic operator and assignment operator -> compound operator
# 2. bitwise operator and assignment operator -> compound operator

x = 6
x = x + 3
print(x)

# x += 3   # x = x + 3

x = 6
x += 3
print(x)


#
x = 9
# x = x - 3  # please rewrite this statement with compound operator
x -= 3
print(x)

#
x = 6
# x = x * 3  # rewrite it
x *= 3


# performance

x = 8

x /=8
print(x)






