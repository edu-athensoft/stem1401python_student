"""
sorted(iterable, key, reverse=False)
reverse= False   ascending
reverse= True    descending
"""
import operator

dict1 = {4:'a', 1:'b', 3:'d', 2:'c'}

# my expected ordered result
# dict1 = {4:'a', 1:'b', 2:'c', 3:'d'}

a = sorted(dict1.items(), key=operator.itemgetter(1))
print(a, type(a))

print(dict(a))


a = sorted(dict1.items(), key=operator.itemgetter(1), reverse=True)
print(a, type(a))

print(dict(a))

