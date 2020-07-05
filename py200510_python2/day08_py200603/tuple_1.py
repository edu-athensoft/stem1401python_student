"""
tuple - create
"""

# create an empty tuple
tuple1 = ()
print(tuple1)


# compare with that in maths
tuple2 = (1)
num2 = 1
print(tuple2)

tuple2 = (1,)
print(tuple2)

# normal
tuple3 = (1,2,3,4,5)
print(tuple3)

# nested tuple
tuple4 = (('a','b'),2,3,4)
print(tuple4)

# mix
tuple5 =  (('a','b'),['c','d'], 3, 4)
print(tuple5)


# tuple is immutable (unchangable)
# update 'c',T OR F?
tuple5[1][0]='ccc'
print(tuple5)

#
listmix = [1,2,(3,4),[5,6]]
# update 3 or 4 , T OR F?
print(listmix[2], type(listmix[2]))
# listmix[2][0] = 'a'
print(listmix)

listmix[2] = ['a','b']
print(listmix)


# list dataset
# application scenario
dataset = [(),(),(),()]

# school, edu institutes
# GIS, map
# financial
# government
# documentation

dataset = ([],[],[],[],[])
# case by case
# games


str = "abc"
for i in str:
    print(i)

# ('a','b','c')

# assignment by pack
x,y,z = (1,2,3)
print(x,y,z)









