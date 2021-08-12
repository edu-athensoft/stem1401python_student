"""
Matrix 3x3
[[1,2,3],[4,5,6],[7,8,9]]

expected result:
1   2   3
4   5   6
7   8   9

"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in matrix:
    for item in row:
        print(item, end='  ')
    print()

# for num in range(1,4):
#     print(num,end=" ")
