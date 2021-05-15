"""
list comprehension
An elegant way to create new list
from an existing list
"""


# an example to make a list with each time being increasing power of 2
# original list: [1,2,3,4,5,6,7,8,9]
# expected result: [1,4,8,16,32,64,128,256,512]

list1 = [1,2,3,4,5,6,7,8,9]

list2 = []
for i in list1:
    # print(i)
    # power of 2
    # print(i,'->',2**i)
    list2.append(2**i)
print(list2)
print()

# list comp.
result = [2**i for i in range(1,10)]
print(result)
