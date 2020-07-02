"""
recursive function

Recursion is the process of defining something in terms of itself.
"""


# factorial
# 1X2X3X4X5X....Xn = ?
# 1x2x3x...x6

# step 3.
def f(n):
    if n <0:
        return "error"
    elif n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * f(n-1)

n = -1
print(f"The factorial of {n} is {f(n)}")

n = 0
print(f"The factorial of {n} is {f(n)}")

n = 1
print(f"The factorial of {n} is {f(n)}")

n = 6
print(f"The factorial of {n} is {f(n)}")

n = 10
print(f"The factorial of {n} is {f(n)}")

