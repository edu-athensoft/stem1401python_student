"""
Homework 5
"""

# 1.

mydict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

dictsum = 0
for i in mydict:
    dictsum += i

print(dictsum)

# 2.

mydict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

dictprod = 1
for i in mydict:
    dictprod *= i

print(dictprod)

# 3.

mydict = {1: 3, 5: 2, 8: 4, 11: 8, 4: 6}

print(max(mydict.values()))
print(min(mydict.values()))

# 4.

mydict = {1: 3,
          5: 3,
          8: 4,
          11: 8,
          4: 6,
          10: 8}

mydict_copy = {}
for i in mydict.items():
    if i[1] not in mydict_copy.values():
        mydict_copy[i[0]] = i[1]

print(mydict_copy)
