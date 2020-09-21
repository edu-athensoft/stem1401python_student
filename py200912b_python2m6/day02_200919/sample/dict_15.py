"""
dictionary - iterating

"""

dict1 = {1:1, 2:4, 3:9, 4:16}

print(type(dict1))
for key in dict1:
    print(key)
print()


for i in dict1.items():
    print(i, type(i))
    print(f"{i[0]}:{i[1]}")
    # print("{}:{}".format(i[0], i[1]))
print()


print(type(dict1.keys()))
for i in dict1.keys():
    print(i)
print()


for i in dict1.values():
    print(i)
print()