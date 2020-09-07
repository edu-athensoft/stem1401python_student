"""
1+2+3+...+10
"""

"""
sum(0) = 0
sum(1) = 1 + sum(0)
sum(2) = 2 + sum(1)
sum(3) = 3 + sum(2)
sum(4) = 4 + sum(3)

sum(n) = n + sum(n-1)


"""

# sumary(10)
def summary(n):
    if n == 1:
        return 1
    return n + summary(n-1)

print("The result is {}",summary(10))


# sumary(9)

def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(10))




