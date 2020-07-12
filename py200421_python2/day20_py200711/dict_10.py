"""
dictionary methods

clear()
copy()

"""

dict1 = {'key1': 1, 'key2': 2, 'key3': 3}
dict2 = dict1.copy()

# test identity
print(dict1 is dict2)

dict2['key3'] = 333
print(dict1)
print(dict2)


# test
dict3 = dict1
print(dict1 is dict3)
dict3['key3'] = 33

print("dict1['key3']=",dict1['key3'])



