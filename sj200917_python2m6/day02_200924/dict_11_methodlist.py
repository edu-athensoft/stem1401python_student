"""
dictionary methods
"""

"""
dict.clear()	    - remove all items
dict.copy()	        - generate a dictionary
dict.fromkeys()     - generate a dictionary
dict.get(key)       - get value by a key ,  v.s. dictname[key]
dict.items()        - get items (key-value pairs)
dict.keys()         - get keys
dict.values()       - get values
dict.pop()          - remove item by key
dict.popitem()      - remove an item and return it
dict.update()       - update dictionary
"""

mydict = {}
mydict = mydict.fromkeys([1,2,3,4])
print(mydict)

mydict = mydict.fromkeys([1,2,3,4],0)
print(mydict)


print(mydict.get(1))
print(mydict.get(5,'unknown'))

