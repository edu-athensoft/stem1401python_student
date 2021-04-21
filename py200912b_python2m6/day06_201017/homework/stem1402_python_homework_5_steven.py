"""
stem1402_python_homework_5_steven
"""

# 1.
dict1 = {
    'a': 123,
    'b': 576,
    'c': 234,
    'd': 334,
    'e': 459,
    'f': 300
}

sum = 0
res = list(dict1.values())
for i in res:
    sum += i

print(f"The sum of all the items in {dict1} is {sum}")
print()
print("-------------------------------------------------------------------------------")

# 2.

dict1 = {
    'a': 12,
    'b': 5,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 30
}

product = 1
res = list(dict1.values())
for i in res:
    product *= i

print(f"The product of all the items in {dict1} is {product}")
print()
print("-------------------------------------------------------------------------------")

# 3.

dict1 = {
    'a': 123,
    'b': 576,
    'c': 234,
    'd': 334,
    'e': 459,
    'f': 300
}

max = 0
min = 0
res = list(dict1.values())

for i in res:
    if i > max:
        max = i
print(f"The maximum value is {max}")

for i in res:
    if i < max:
        max = i
    min = max
print(f"The minimum value is {min}")
print()
print("-------------------------------------------------------------------------------")

# 4.

dict1 = {
    'a': 123,
    'b': 576,
    'c': 123,
    'd': 334,
    'e': 123,
    'f': 300
}

dict2 = {}


for key, value in dict1.items():
    if value not in dict2.values():
        dict2[key] = value

print(f"Dictionary without duplicates : {dict2}")
