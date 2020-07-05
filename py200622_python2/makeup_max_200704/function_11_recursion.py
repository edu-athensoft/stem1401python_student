"""
recursive function
"""


# factorial of n (number)
# n!
# n! = n x (n-1) x (n-2) x (n-3) x (n-4) x (n-5) x..... x 2, 1


# 1 .. n
"""
n  = 6
product = 1
for i in range(1, n+1):
    product *= i

print(product)
"""

# 6! = 6x 5 x4 x3 x2 x1
# 6! = 6 x 5!
# 5! = 5 x 4!
# 4! = 4 x 3!
# 3! = 3 x 2!
# 2! = 2 x 1!
# 1! = 1

#
# n! = n * (n-1)!
# f(n) = n!


# f(6) = 6 * f(5)


def factorial(n):
    if n==1 or n==0:
        return 1
    elif n<0:
        return "error"
    return n * factorial(n-1)

print(factorial(6))
print(factorial(1))
print(factorial(0))
print(factorial(-1))


# homework 1
# using recursive function to calculate the sum of number sequence from 1 to 100

# homework 2
# using recursive function to get the nth item of a Fibonacci sequence
# n > 2, where n is an positive integer









