"""
remove items from a list

1. del  keyword (delete)
2. clear()
3. remove()
"""

# case 1. remove one item
mylist = ['p','r','o','b','l','e','m']
del mylist[2]
print(mylist)

# case 2. delete multiple items
mylist = ['p','r','o','b','l','e','m']
# removing 'r','o','b
del mylist[1:4]
print(mylist)

# del mylist
# print(mylist)


# clear()
mylist = ['p','r','o','b','l','e','m']
mylist.clear()
print(mylist)


# 3. remove(value)
mylist = ['p','r','o','b','l','e','m','o']
mylist.remove('o')
print(mylist)
mylist.remove('o')
print(mylist)
# mylist.remove('o')
# print(mylist)
print()


# 4. pop(index)
mylist = ['p','r','o','b','l','e','m','o']
mylist.pop(0)
print(mylist)
mylist.pop(100)
print(mylist)



