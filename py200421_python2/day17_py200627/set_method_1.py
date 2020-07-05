"""
set method

add()
clear()
copy()	- return a copy of set

implement - to work it out, to figure it out, to write the detail
"""


# copy()
A = {1,2,3,4,5}
# copy A to B
B = A.copy()
print(B)

# our solution of copy
C = set()
for i in A:
    print(i)
    C.add(i)

print(C)
print(C is A)


# upgrade our code
def mycopy(A):
    C = set()
    for i in A:
        print(i)
        C.add(i)
    return C

D = mycopy(A)
print("D",D)







