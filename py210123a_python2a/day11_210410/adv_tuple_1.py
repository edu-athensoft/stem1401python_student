"""
create a tuple
tuple is immutable
"""

# identity and equivalence
tuple1 = (1,2,3,4,5)
print(type(tuple1), id(tuple1))

tuple2 = (1,2,3,4,5)
print(type(tuple2), id(tuple2))

print(tuple1 is tuple2)
print(tuple1==tuple2)

# compare with list
list1 = [1,2,3,4,5]
print(type(list1), id(list1))

list2 = [1,2,3,4,5]
print(type(list2), id(list2))

print(list1 is list2)
print(list1==list2)


# create a tuple with only one element
# tuple3 = (2)      # not a tuple
tuple3 = (2,)
print(type(tuple3))


# mix
tuple4 = (1, 2.5, 'abc', True)
print(tuple4)

# mix - collection
tuple5 = ("mouse", [8, 4, 6], (1, 2, 3))
print(tuple5, type(tuple5))

# tuple5[0] = 'cat'         # error
# tuple5[1] = [8, 4, 6]     # error
# tuple5[2] = (1, 2, 3)     # error

tuple5[1][0] = 80   # ok
print(tuple5)


# application 1
# game save
save1 = []
save2 = []
save3 = []
save1 = []  # reassigned save4
saveslots = (save1, save2, save3)
saveslots = (save1, save2, save3)


# application 2
# student profiles
# student administrator
stu1 = ('name1','dob1','stuid1')
stu2 = ('name2','dob2','stuid2')
stu3 = ('name3','dob3','stuid3')
list1 = [stu1, stu2, stu3]



# create a tuple by packing
tuple6 = 'cat','dog','duck'
print(tuple6, type(tuple6))

# str1, str2, str3 = 'cat','dog','duck'
# print(str1, str2, str3)

# unpacking
x, y, z = tuple6
print(x,y,z)
print(x)
print(y)
print(z)





