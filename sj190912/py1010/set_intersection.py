# set intersection

A = {1,2,3,4,5}
B = {4,5,6,7,8}

C = A & B
print(C)


A = {1,2,3,4,5}
B = {6,7,8,9}

C = A.intersection(B)
print(C)

C = B.intersection(A)
print(C)

C = A & B
print(C)