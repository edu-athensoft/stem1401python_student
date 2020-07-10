"""
Homework 5
"""


def fibonacci(x):
    if x < 0:
        return "error"
    elif x == 0:
        return 0
    elif x == 1 or x == 2:
        return 1
    else:
        for number in range(x):
            return fibonacci(x - 1) + fibonacci(x - 2)


print(fibonacci(3))
