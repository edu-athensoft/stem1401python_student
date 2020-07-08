"""
Python dictionary
Sorting by key

functions:
sorted()
list()
map()
list comprehension

references:
https://blog.csdn.net/buster2014/article/details/50939892
"""

# option 1
def sortedDictValues1(mydict):
    items = mydict.items()
    # items.sort()
    sorted(items)
    return [value for key, value in items]


# option 2
def sortedDictValues2(mydict):
    keys = mydict.keys()
    # keys.sort()
    sorted(keys)
    return [mydict[key] for key in keys]


# option 3
def sortedDictValues3(mydict):
    keys = mydict.keys()
    # keys.sort()
    sorted(keys)
    return map(mydict.get, keys)


# option 4
def sortedDictValues4(mydict):
    return [(k,mydict[k]) for k in sorted(mydict.keys())]



# main program
demo_dict = {
    1: "c",
    2: "a",
    3: "b"
}
print("Original dictionary is: {}".format(demo_dict))
print()

# test 1
print("[info] testing sortedDictValues1()")
print(sortedDictValues1(demo_dict))
print()

# test 2
print("[info] testing sortedDictValues2()")
print(sortedDictValues2(demo_dict))
print()

# test 3
# list(map) - show data in a map by converting to a list
print("[info] testing sortedDictValues3()")
print(list(sortedDictValues3(demo_dict)))
print()

# test 4
print("[info] testing sortedDictValues4()")
print(list(sortedDictValues4(demo_dict)))
print()
