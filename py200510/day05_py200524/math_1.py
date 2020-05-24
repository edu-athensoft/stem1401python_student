"""
module math
"""
import math

# function
# trigonometry
print("sin90",math.sin(math.pi/2))
print()


# logarithms
print("log10",math.log10(1000))
print()

# factorial
print(math.factorial(6))
print("6! = {}".format(math.factorial(100)))

prod = 1
for i in range(1,101):
    prod *= i
print(prod)

# constant, name
print(math.pi)
print(round(math.pi,2))


