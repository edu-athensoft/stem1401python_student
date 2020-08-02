"""
Display the 9x9 multiplication table

1 X 1 = 1
1 X 2 = 2   2 X 2 = 4
1 X 3 = 2   2 X 3 = 4   3 X 3 = 9
...
...
1 X 9 = 2   2 X 9 = 18   3 X 9 = 27     4 X 9 = 36  ...     9 X 9 = 81


hints:
for-loop (nested for-loop)
string.format()

"""
# row 1
for i in range(1,2):
    print(i, 1,  end="  ")
print()

# row 2
for i in range(1,3):
    print(i, 2, end="  ")

print()

# row 3
for i in range(1,4):
    print(i, 3, end="  ")
print()

# row 4
for i in range(1,5):
    print(i, 4, end="  ")

# row 9
for i in range(1,10):
    print(i, 9, end="  ")






# for i in range(1,10):
#     # print(i)
#     for j in range(1,i+1):
#         print(j, i)

