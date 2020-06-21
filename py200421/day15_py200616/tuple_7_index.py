"""
tuple index()
"""

tuple1 = (1,2,3,1,2,4,1,2,5,6,4,2,3,4,9,6,7,7,7)

pos = tuple1.index(6)
print("The position of 6 is {}".format(pos))

pos = tuple1.index(5)
print("The position of 5 is {}".format(pos))

pos = tuple1.index(5)
print("The position of 5 is {}".format(pos))

pos2 = tuple1.index(5, 2)
print("The next position of 5 is {}".format(pos2))

pos3 = tuple1.index(5, 2, 14)
print("The next position of 5 is {}".format(pos3))

pos = tuple1.index(6)
print("The position of 6 is {}".format(pos))

pos2 = tuple1.index(6, 10)
print("The next position of 6 is {}".format(pos2))

pos3 = tuple1.index(6, 10, 17)
print("The next position of 6 is {}".format(pos3))


# [Homework]
# how to search for the second target number in a tuple
