"""
author: Ken
"""

# Question 1
def secondelement(el):
    return el[1]

list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

list1 = [1,4,6,3,6,8]
list1.sort(key=secondelement)

print(list1)