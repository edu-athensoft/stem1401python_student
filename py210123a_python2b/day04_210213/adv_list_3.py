"""
how to access items from a list

access item(s) from a complex(nested) list

"""


list2 = [345,4654,['abc','fff','xyz'],565,789,9,12213]

# option 1
# how to access 'fff'
# step 1. to get ['abc','fff','xyz']
A = list2[2]
print(A)

# step 2. to get 'fff'
res = A[1]
print(res)

print('===========')

# option 2
# combine
res2 = list2[2][1]
print(res2)



# ex.
list3 = [[3,4],[5,6],[2,3]]
# how to get the item of 2

res = list3[2][0]
print(res)


# example
list4 = [[3,[55,66]],[5,6],[2,3]]
res = list4[0][1][0]
print(res)





