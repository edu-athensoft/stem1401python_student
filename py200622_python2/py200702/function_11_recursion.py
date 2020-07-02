"""
recursive function

Recursion is the process of defining something in terms of itself.
"""


# factorial
# 1X2X3X4X5X....Xn = ?
# 1x2x3x...x6

# step 1.
# result = 1
# N = 6
# for i in range(1,N+1):
#     result *= i
# print(f'result = {result}')


# step 2.
def factorial(n):
    result = None
    if n <0:
        result = 'error'
    elif n==0:
        result = 1
    elif n==1:
        result =1
    else:
        f = 1
        for current_number in range(1, n + 1):
            f *= current_number
        result = f
    return result


print(factorial(-2))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(6))

print(factorial(10))

