"""
set operation
union()
intersection()
difference()
Symmetric Difference

"""



A = {'card1','card2','card3'}
B = {'card1','card2','card4'}


# set difference
# A - B
result = A - B
print("A - B is {}".format(result))

result = A.difference(B)
print("A - B is {}".format(result))

# B - A
result = B - A
print("B - A is {}".format(result))

result = B.difference(A)
print("B - A is {}".format(result))


# symmetric difference
# ^
result = A ^ B
print("A ^ B is {}".format(result))

result = A.symmetric_difference(B)
print("A ^ B is {}".format(result))

result = B ^ A
print("B ^ A is {}".format(result))

result = B.symmetric_difference(A)
print("B ^ A is {}".format(result))