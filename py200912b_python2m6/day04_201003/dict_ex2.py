"""
sorting in ascending order
numeric : from the smallest to the biggest
string:   A->Z a->z

sorting in descending order

"""

"""
a < b < c
ab < ac
acb > abc
ab < abb
"""

# sorting a dictionary
d = {'ca': 2, 'ab': 4, 'bb': 3, 'b': 1, 'aa': 0}
print("before:",d)
# sorted() - built-in
result = sorted(d.items())
# print(result, type(result))

# convert to dictionary
sorted_d = dict(result)
print("after:",sorted_d)
