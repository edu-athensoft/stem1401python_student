"""
1. Write a Python program to generate a 3*2*3 3D array whose each element is *.

"""
arr = [[['*','*','*'],['*','*','*']] ,
       [['*','*','*'],['*','*','*']] ,
       [['*','*','*'],['*','*','*']]]

print(arr)


# input/setting
X = 4
Y = 5
Z = 6

# 1. ['*','*','*']
arr1 = []
for i in range(X):
    arr1.append('*')

# 2. [['*','*','*'],['*','*','*']]
arr2 = []
for j in range(Y):
    arr2.append(arr1)

# 3. [[['*','*','*'],['*','*','*']], [['*','*','*'],['*','*','*']], [['*','*','*'],['*','*','*']]]
arr3 = []
for k in range(Z):
    arr3.append(arr2)


# output
print(arr3)

