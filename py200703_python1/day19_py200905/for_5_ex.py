"""
for loop ex
"""


# sum from 1..1000

sum = 0
for i in list(range(1,1001)):
    sum = i + sum

print("The sum of the sequence is {}".format(sum))


sum = 0
for i in range(1,1001):
    # sum = i + sum
    sum += i

print("The sum of the sequence is {}".format(sum))


# prod from 1..20
prod = 1
for i in range(1,21):
    prod *= i

print("The prod of the sequence is {}".format(prod))

