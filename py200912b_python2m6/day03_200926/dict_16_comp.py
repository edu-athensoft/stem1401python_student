"""
dictionary comprehension

1. Write a Python program to generate and print a dictionary that contains a number (between 1 and n)
in the form (x, x*x).
e.g. User inputs 5
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

"""
n = 10
for i in range(1,n+1):
    key = i
    value = key * key
    print(key, value)

# {key: key*key }
# {key: key*key for key in range(1, n+1)}
mydict = {key: key*key for key in range(1, n+1)}

print(mydict)


# ex 1.
"""
{
    1:  3,
    2:  5,
    3:  7,
    4:  9,
    ...
    10: 21
}"""

# version 1.
mydict2 = {k: 2*k+1 for k in range(1,11)}
print(mydict2)

# version 2.
n = 10
mydict2 = {k: 2*k+1 for k in range(1,n+1)}
print(mydict2)

# version 3.
def getdict(n):
    return {k: 2*k+1 for k in range(1,n+1)}

# getdict(2)
# getdict(5)
# getdict(10)

# automated
testdata = [2,5,10,4,7,9]

for i in testdata:
    getdict(i)






