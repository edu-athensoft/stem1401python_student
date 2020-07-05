"""
list - methods(funtions)
"""

# index()

list1 = [1,2,34,6,'abc',67,7,8,8,9,9,'abc']

target= 'abc'

# for i in range(len(list1)):
#     if list1[i] == target:
#         print(i,list1[i])
print("=== index() ===")
print(list1.index(target), target)


# count()
print("=== count() ===")
print(list1.count(target), target)


# sort()
# list_a = [3,4,2,1]
list_a = ['ab3','ab4','ba2','ba1']
# list_a = [1,'a',2,'c']
list_a.sort()
print(list_a)

list_a.sort(reverse=True)
print(list_a)

# reserve()
list_a = [3,4,2,1]
list_a.reverse()
print(list_a)


# copy()
list_b = list_a.copy()
print(list_b)

print(list_a is list_b)
print(list_a == list_b)





