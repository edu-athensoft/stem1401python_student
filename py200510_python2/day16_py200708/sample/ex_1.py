"""
dictionary - ex 1

by key
"""


demo_dict = {
    3: "c",
    2: "a",
    1: "b"
}

# sorting by key
# converting to iterable
items = demo_dict.items()
print(items, type(items))

b = list(items)
print(b, type(b))

# sorted(iterable, key, reverse=False)
c = sorted(items)
print(c)
print()

# before
print([value for key, value in items])
print([(key, value) for key, value in items])
print()

# after
print([value for key, value in c])
print([(key, value) for key, value in c])





