"""
membership operator

in, not in
"""
# case 1. list
list1 = [1,2,3,4,5,6,7]
print(8 in list1)
print(8 not in list1)
print()

print(3 in list1)
print(3 not in list1)
print()

# case 2. tuple
tuple1 = ('a','b','c','d')
print('b' in tuple1)
print('b' not in tuple1)
print()

print('z' in tuple1)
print('z' not in tuple1)
print()

# case 3. set
set1 = {'pencil','eraser','crayon','sharpie'}
print('eraser' in set1)
print('eraser' not in set1)
print()

print('ruler' in set1)
print('ruler' not in set1)
print()

# case 4. dict
dict1 = {"w":"word", "s":'sentence', "a":"alphabet", "e":"encyclopedia"}
print('slang' in dict1)
print('slang' not in dict1)
print()

print('w' in dict1)
print('w' not in dict1)
print()

print('word' in dict1)
print('word' not in dict1)







