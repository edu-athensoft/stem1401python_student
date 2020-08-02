"""
matrix (3x4)

1,  2,   3,    4
5,  6,   7,    8
9,  10,  11,   12


to calculate the average of this matrix

"""

"""
plan:

step 1. to choose a proper data structure to represent the data set
step 2. to add all the items in the matrix together
step 3. to calculate the average
step 4. to output the result
"""

# step1.
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# matrix = [1,2,3,4,5,6,7,8,9,10,11,12]

# step2.
summary = 0
count = 0

for row in matrix:
    # print(row)
    for col in row:
        # print(col)
        summary = summary + col
        count = count + 1

# step3.
num = count
avg = summary / num

# step4.
print("The average is {}".format(avg))
print("There are {} items in the matrix".format(num))



