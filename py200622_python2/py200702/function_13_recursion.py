"""
recursion function - exercise

please calculate the sum of a number sequence from 1 to N by step of 1

"""

# by Ken
def sum_finder(n):
    if n < 1:
        return "error"
    elif n == 1:
        return 1
    else:
        return n + sum_finder(n - 1)

n = 10
print(f"The sum of {n} is {sum_finder(n)}")


# by Neison
def addition(x):
    if x == 1:
        return 1
    elif x < 1:
        return "error"
    else:
        return x + addition(x - 1)


n = 100
print(f"The sum of numbers 1 to {n} is {addition(n)}")


# by Yixuan
def f(n):
    if n < 1:
        return "error"
    elif n == 1:
        return 1
    else:
        return n + f(n - 1)

n = 100
print(f"The factorial of {n} is {f(n)}")


# by Kevin
def summation(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + summation(n - 1)


n = 100
# print(f"The summary of {n} is {summation(n)}")
print(f"The summation of {n} is {summation(n)}")


# by Steven
def sum(n):
    if n < 0:
        return "Error"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum(n - 1)

n = 10
print(f"The sum of numbers from 1 to {n} is {sum(n)}")
