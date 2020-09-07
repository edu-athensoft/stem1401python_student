"""
accessing items or elements

index
indexing
by index
index starts from 0
"""

friends = ['Peter','Adam','Amy','Jack','Tom']

print(friends[0])

print(friends[1])

print(friends[2])

print(friends[3])

print(friends[4])

# IndexError: list index out of range
# print(friends[5])


# to access an item of a nested list
mylist2 = [1,2,3,[4,5,6]]
# get the 5
i3 = mylist2[3]
print(i3)
print(i3[1])

print(mylist2[3][1])


# ex. get the number of 23 from the matrix

matrix = [
    [11,12,13,14],
    [21,22,23,24],
    [31,32,33,34]
]
print()

# application:  to place a monster or item in a map

# to get the number of 5 - 3-dimensional structure
dataset = [
    [[1],[2],[3]],
    [[4],[5],[6]],
    [[7],[8],[9]]
]

print(dataset[1][1][0])


# negative index
# RTL starts from -1
friends = ['Peter','Adam','Amy','Jack','Tom']
print(friends[-1])
print(friends[-2])
print(friends[-3])
print(friends[-4])
print(friends[-5])


# the first element
print(friends[0])

# the last element
print(friends[-1])
print(friends[4])
# len() - length or size of a list
print("The length of the list is {}".format(len(friends)))
print(friends[len(friends)-1])







