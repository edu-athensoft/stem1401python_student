"""
ex.

[1,2,3,4,5,6,7,8]

double each item and get this
[2,4,6,8,10,12,14,16]

"""


list2 = [1,2,3,4,5,6,7,8]

result = [2*i for i in list2]

print(result)

result = [2*i for i in [1,2,3,4,5,6,7,8]]

print(result)