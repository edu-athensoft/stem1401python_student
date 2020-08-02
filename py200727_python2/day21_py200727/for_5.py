"""
print out the coord for items of a matrix

3x3
3 rows
3 cols
9 items
"""

# write a program to print out all the
# coord of the given matrix

"""
(0,0), (0,1), (0,2)
(1,0), (1,1), (1,2)
(2,0), (2,1), (2,2)
"""

# for y in range(0,3):
#     print("({}, {})".format(0, y), end=" ")
#
# print()
#
# for y in range(0,3):
#     print("({}, {})".format(1, y), end=" ")
#
# print()
#
# for y in range(0,3):
#     print("({}, {})".format(2, y), end=" ")


for x in range(0, 3):
    for y in range(0, 3):
        print("({}, {})".format(x, y), end=" ")
    print()


# kevin
for row in range(0,3):
    for col in range(0,3):
        print(("({},{})".format(row,col)), sep=",",end="")
    print()

