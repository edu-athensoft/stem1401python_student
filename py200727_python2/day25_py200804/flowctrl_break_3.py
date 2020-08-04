"""
If break statement is  inside a nested loop, break will terminate the innermost loop.

to prove the break statement just terminate the innermost loop structure.

step 1. create a nested loop structure with at least 2 levels
    3 options: for-loop, while-loop, for-while-loop

step 2. set a break statement at proper location

step 3. run your program and check out the result to draw a conclusion
"""


matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# jump out of the inner loop
for row in matrix:
    for col in row:
        if col == 6:
            break
        print(col)
    print()

print("=== 2nd for loop with break ===")
# jump out of the outer loop
for row in matrix:
    for col in row:
        print(col)
        if col == 6:
            break;
    # print("col in outer loop is {}".format(col))
    if col == 6:
        break
    print()



