"""
dictionary  keys()

hints:

try out keys() by writing trail code

create an example to test and run

"""


mydict = {1: 'a',
          2: 'b',
          3: 'c',
          4: 'd',
          4: 'e'}
print(mydict)

# kevin
print("Before:", mydict)

for item in mydict.keys():
    print(item, type(item))


# keys()
result = mydict.keys()
print(result, type(result))

# dict_keys -> list
result2 = list(mydict.keys())
print(result2, type(result2))


