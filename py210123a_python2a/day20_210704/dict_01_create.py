"""
dict
create

key:  immutable value
    number
    string
    tuple
    other immutable type
"""

# create a normal dictionary
dict1 = {
    1: 'a',
    2: 'b',
    3: 'c'
}

print(dict1)
# output {1: 'a', 2: 'b', 3: 'c'}

# question
# one value for one key
# key must be unique
# values are not neccessary different
dict2 = {
    1: 'a',
    2: 'a',
    3: 'a'
}

print(dict2)


# overwriting key-value pair
dict3 ={
    1: 'a',
    2: 'a',
    3: 'a',
    3: 'b'
}

print(dict3)

dict3b ={
    1: 'a',
    2: 'a',
    3: 'b',
    3: 'a'
}

print(dict3b)

# the case that a key is None
dict4a = {
    1: 'a',
    2: 'b',
    3: 'c',
    None: 'no value'
}

print(dict4a)


dict4a2 = {
    1: 'a',
    2: 'b',
    3: 'c',
    None: 'no value 1',
    None: 'no value 2'
}

print(dict4a2)

# the case that a value is None
dict4b = {
    1: 'a',
    2: 'b',
    3: 'c',
    4:  None,
    5:  None
}
print(dict4b)