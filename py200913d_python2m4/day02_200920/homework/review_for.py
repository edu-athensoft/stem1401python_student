"""
*
*  *
*  *  *
*  *  *  *
*  *  *  *  *
"""

"""
1st one *
2nd two *
3rd three *
4th four *
5th five *

step 1. print out 5 lines
step 2. print * for each row
"""

# trail 1
# for row in range(5):
#     print(row)

# trail 2
# for row in range(1,6):
#     print("print * for row #",row)

# trail 3
# for row in range(1,6):
#     print("print * for row #",row)
#     for n in range(1,row+1):
#         print('*')

# trail 4
for row in range(1,6):
    # print("print * for row #",row)

    for n in range(1,row+1):
        print('*', end=" ")
    print()

"""
print out 5 rows:
    in each row, print out stars for the times of row number
    break line
"""