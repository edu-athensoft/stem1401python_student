"""
lambda, high order function
"""

# input a number
# output a mulplication table  (a x 1 to a x 10)
"""
input :  3

3 x 1 = 3
3 x 2 = 6
...
3 x 10 = 30
"""


# return a lambda function
def table(n):
    return lambda a : a * n


# input a number
n = int(input("Enter an integer (n>0):"))

# get the function with n
b = table(n)

for i in range(1, 11):
    print(f"{n} x {i} = {b(i)}")




