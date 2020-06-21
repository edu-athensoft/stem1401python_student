"""
dictionary operation

a collection of key:value pair

syntax
{
    key1: value1,
    key2: value2,
    key3: value3
    ...
}

dictionary - mutable
key - unique, immutable literal
value - not necessarily unique, mutable

features:
mapping
look up

"""


# create a dictionary (dict)
dict1 = {}
print(dict1, type(dict1))

dict2 = {"a": "apple", "b": "bell", "c":"cell"}
print(dict2)

dict3 = {
    "a": "apple",
    "b": "bell",
    "c": "cell"
}
print(dict3)
print()

# dict()
my_dict = dict({"a": "apple", "b": "bell", "c":"cell"})
print(my_dict,type(my_dict))

my_dict = dict([("a","apple2"),("b","bell2")])
print(my_dict,type(my_dict))

my_dict = dict([["a","apple2"],["b","bell2"]])
print(my_dict,type(my_dict))

my_dict = dict((("a","apple2"),("b","bell2")))
print(my_dict,type(my_dict))