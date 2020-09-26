"""
Homework 2
"""


# 1.
def square(input_num):
    output = {}
    for i in range(1, input_num + 1):
        output[i] = i * i

    print(output)


square(5)

# 2.
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

dict1.update(dict2)
dict1.update(dict3)

print(dict1)

# 3.
person_profile = {
    'empid': '0001',
    'name': 'Peter',
    'ismanager': True,
    1: 'availabe',
    2: 'long-term'
}

person_profile_copy = {}

for i in person_profile:
    if isinstance(i, int):
        pass
    else:
        person_profile_copy[i] = person_profile[i]


# for i in person_profile:
#     if not isinstance(i, int):
#         person_profile_copy[i] = person_profile[i]

#
# for i in person_profile:
#     if isinstance(i, int):
#         person_profile.pop(i)


print(person_profile_copy)