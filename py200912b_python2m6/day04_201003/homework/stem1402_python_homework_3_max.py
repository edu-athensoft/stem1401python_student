"""
Homework 3
"""

# 1.
dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {}


def dictchecker(dictionary):
    if len(dictionary) == 0:
        return "Length is 0"
    else:
        return "Length is not 0"


print(dictchecker(dict1))
print(dictchecker(dict2))


# 2.
def square(num):
    mydict = {key: key * key for key in range(1, num + 1)}

    return mydict


print(square(5))
print(square(11))

# 3.
mydict = {7: 11, 25: 12, 745: 34, 6: 86, 13: 8, 40: 58, 93: 72, 38: 66}


def maxandmin(dictionary):
    return max(mydict.values()), min(mydict.values())


print(maxandmin(mydict))
