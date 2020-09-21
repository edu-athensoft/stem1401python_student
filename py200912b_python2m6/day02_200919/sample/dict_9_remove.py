"""
dictionary removing elements from a dictionary

pop() - removes an item with the provided key and returns the value
popitem() - can be used to remove and return an arbitrary (key, value) pair
clear() - remove all items
"""

my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}

# remove an item by using pop()
my_dict.pop(1)
print(my_dict)

my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
my_dict.pop(3)
print(my_dict)


# sample
my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
value = my_dict.pop(3)
print(value)
print(my_dict)

# popitem()



# qijun
my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}

my_dict.popitem()
print(my_dict)


# issa
# popitem()

my_dict = {
    '1': 1,
    '2': 4,
    '3': 9,
    '4': 16,
    '5': 25
}

value1 = my_dict.popitem()
print(value1, my_dict)

my_dict = {
    '1': 1,
    '2': 4,
    '3': 9,
    '4': 16,
    '5': 25
}

value2 = my_dict.popitem()
print(value2, my_dict)

# zihan
my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
# value = my_dict.popitem(1)
value = my_dict.popitem()
print(value)
print(my_dict)


# remove all items
my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
my_dict.clear()
print(my_dict)

# del
my_dict = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25
}
del my_dict[1]
print(my_dict)

# del my_dict[1]
# print(my_dict)

del my_dict[2]
print(my_dict)

# del all items and the dictionary itself
del my_dict
# print(my_dict)



