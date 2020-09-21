"""
dictionary
update()
"""

dict1 = {1:"one", 2:"three"}


# case 1. update with another dictionary
dict2 = {2:"two"}
dict1.update(dict2)
print(dict1)

dict3 = {3:"three"}
dict1.update(dict3)
print(dict1)
print()









# case 2. update with iterable
# list2 = [2,'two']
list2 = [[2,'two']]
dict1.update(list2)
print(dict1)

# tuple is immutable
dict1 = {1:"one", 2:"three"}
list3 = [[2,'two'],[4,'four']]
dict1.update(list3)
print(dict1)



