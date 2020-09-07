"""
1 + 2 + 3 + 4 + ... + 10 + (996)

f(n) = n + f(n-1)

[Previous line repeated 996 more times]
RecursionError: maximum recursion depth exceeded

def f(n):
    return n + f(n-1)

print(f(10))

advantages and disadvantages
advantages
1. recursive functions make the code look clean and elegant
2. a complex task can be broken down into simpler sub-problems using recursion
3. sequence generation is easier with recursion than using some nested iteration

disadvantages
1. sometimes the logic behind recursion is hard to follow through
2. recursive calls are expensive (inefficient) as they take up a lot of memory and time
3. recursive function are hard to debug

"""

def f(n):
    if n == 1:
        return 1
    return n + f(n-1)

print(f(9980))



# solution
# def sum_finder(n):
#     if n < 1:
#         return "error"
#     elif n == 1:
#         return 1
#     else:
#         return n + sum_finder(n - 1)
#
# n = 10
# print(f"The sum of {n} is {sum_finder(n)}")



