"""
map()
"""

original = [1,2,3,4]
target = []

# [1, 4, 9, 16]

# solution 1
for i in original:
    # print(i**2)
    target.append(i**2)
print(target)


# solution 2
result = map(lambda x: x**2 , original)
print(result, type(result))

result = list(result)
print(result)

print(list(map(lambda x: x**2 , original)))


# ex1.
original = [1,2,3,4,5,6]
# target = [3, 5,7, 9, 11,13]

# kevin
print(list(map(lambda x : 2*x + 1, original)))




