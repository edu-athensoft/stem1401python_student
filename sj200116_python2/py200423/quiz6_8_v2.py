"""

"""
"""
matrix = [[11,12,13,14],[21,22,23,24],[31,32,33,34]]
# print(matrix)

for row in matrix:
    # print(row)
    for col in row:
        print(col, end="\t")
    print()

print()

matrix = [[11,12,13],[21,22,23],[31,32,33]]
# print(matrix)

for row in matrix:
    # print(row)
    for col in row:
        print(col, end="\t")
    print()
"""


def showmatrix(matrix):
    for row in matrix:
        for col in row:
            print(col, end="\t")
        print()


# input data
mtr1 = [[11,12,13,14],[21,22,23,24],[31,32,33,34]]
mtr2 = [[11,12,13],[21,22,23],[31,32,33]]
mtr3 = [[11,12],[21,22,23,24],[31,32,33]]
showmatrix(mtr1)
print()
showmatrix(mtr2)
print()
showmatrix(mtr3)


