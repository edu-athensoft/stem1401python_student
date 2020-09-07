"""
nested for loop
"""

# create a matrix by 3X4
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]


for row in matrix:
    # print(row)
    for item in row:
        print(item)

