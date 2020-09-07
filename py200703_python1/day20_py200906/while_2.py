"""
while loop
"""

# print out 1 to 10

n = 1

while n < 10 + 1:
    print(n)
    # n = n + 1
    n += 1


# print out 10 to 1

n = 10
while n > 0:
    print(n)
    # n = n - 1
    n -= 1


print(list(range(10,0,-1)))
