"""
remove item(element) from a set

discard()
remove()
clear()
del - keyword
"""

# step 1. create a set with some items
set1 = {'1', '2', '3'}

# step 2. try out discard()
set1.discard('1')
print(set1)

set1.discard('1')
print(set1)
print()

# step 3. try out remove()
set1.remove('2')
print(set1)

# KeyError: '2'
# set1.remove('2')
# print(set1)

# step 4. compare
# conclusion


# clear()
# remove all the items in a set
set1 = {'1', '2', '3'}
set1.clear()
print(set1)

set1.clear()
print(set1)


# del
# delete
del set1
print(set1)


