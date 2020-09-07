"""
Recursion
is the process of defining something in terms of itself

1. example
2. example - recursive

"""

# 1 X 2 X 3 X 4 X 5
# prod = 1
#
# for i in range(1,6):
#     prod = prod * i
#
# print(prod)


def f(n):
    if n == 1:
        return 1
    return n * f(n-1)

print(f(5))