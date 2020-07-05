"""
change or update
"""
odd = [2, 4, 6, 8]

# case 1. update one item of value
odd[0] = 1
print(odd)

# odd[1] = 3
# print(odd)
#
# odd[2] = 5
# print(odd)
#
# odd[3] = 7
# print(odd)

# case 2. update items of value
odd[1:] = [3,5,7]
print(odd)

odd[1:4] = [3,5,7]
print(odd)

odd[1:4] = [3,5]
print(odd)

odd = [1, 4, 6, 8]
odd[1:4] = [3,5,7,9]
print(odd)
