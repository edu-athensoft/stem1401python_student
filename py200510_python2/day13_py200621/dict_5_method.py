"""
dictionary methods

items()
keys()
values()

"""

my_dict1 = {1:"mon",2:"tue", 3:"wed", 4:'thu', 5:"fri", 6:"sat", 7:"sun"}

# items()
myitems = my_dict1.items()
print(myitems, type(myitems))

myitems = list(myitems)
print(myitems, type(myitems))

for item in myitems:
    print(item[0],item[1])

# keys()
mykeys = my_dict1.keys()
print(mykeys, type(mykeys))

mykeys = list(mykeys)
print(mykeys, type(mykeys))

# values()
myvalues = my_dict1.values()
print(myvalues, type(myvalues))

myvalues = list(myvalues)
print(myvalues, type(myvalues))

