"""
add items to a list
"""

# list: [1,22,3,46,5,62,7,88,9,104]
# pick up all the even number from the list and print them out

# add one item to a list
# append(value)

orginal = [1,22,3,46,5,62,7,88,9,104]
result = []

for i in orginal:
    if i%2 == 0:
        result.append(i)

print(result)

