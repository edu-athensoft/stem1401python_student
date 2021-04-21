"""
1. Write a Python program to generate a 3*2*3 3D array whose each element is *.

"""

"""
1D Array  (one dimensional)
2D Array  (two dimensional)  Matrix
3D Array

i.e.

1D  ->  [3,2,1,4,5,6,7,8,9,10]
2D  ->  [[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]]
3D  ->  
"""



arr = [[['*','*','*'],['*','*','*']] ,
       [['*','*','*'],['*','*','*']] ,
       [['*','*','*'],['*','*','*']]]

print(arr)

# how to generate a 3d array
# 1. ['*','*','*']
# hard code

# arr1 = ['*','*','*']
# print(arr1)

# using for-loop
arr1 = []
# arr1.append('*')
# arr1.append('*')
# arr1.append('*')

X = 4
for i in range(X):
    arr1.append('*')

print(arr1)

# 2. [['*','*','*'],['*','*','*']]
# arr1 = []
# for i in range(3):
#     arr1.append('*')

arr2 = []
Y = 5
for j in range(Y):
    arr2.append(arr1)

print(arr2)


# 3. [[['*','*','*'],['*','*','*']], [['*','*','*'],['*','*','*']], [['*','*','*'],['*','*','*']]]

arr3 = []
Z = 6
for k in range(Z):
    arr3.append(arr2)

print(arr3)

