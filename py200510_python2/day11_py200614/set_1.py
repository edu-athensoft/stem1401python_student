"""
set

items of set are immutable
set itself is mutable
"""

# testlist = [(),(),()]


# create a set
set1 = {1,2,3,4}

# create an empty set
set2 = {}
list2 = []
print("empty set {}, the type is {}".format(set2, type(set2)))
set2 = set()
print("empty set {}, the type is {}".format(set2, type(set2)))

# create a special set
# set3 = {1,2,True,'abc',(1,2),[3,4]}
# TypeError: unhashable type: 'list'


