"""
1. Write a Python program to generate a 3*2*3 3D array whose each element is *.

"""



def create3dArray(x, y, z):
    # 1.
    arr1 = []
    for i in range(x):
        arr1.append('*')

    # 2.
    arr2 = []
    for j in range(y):
        arr2.append(arr1)

    # 3.
    arr3 = []
    for k in range(z):
        arr3.append(arr2)

    return arr3

# main program
# input/setting
X = 3
Y = 2
Z = 3

my3dArray = create3dArray(X, Y, Z)
# output
print(my3dArray)

X = 4
Y = 5
Z = 6

my3dArray = create3dArray(X, Y, Z)
# output
print(my3dArray)



