"""
access element

index , starts from 0, end with the (length -1)
indexing

"""

# 9 items/elements
mylist = [1,2,3,4,5,6,7,8,9]

# access element with index
# the first element
a0 = mylist[0]
print(a0)
print(mylist[0])

a4 = mylist[4]
print(a4)
print(mylist[4])

# the last element
a8 = mylist[4]
print(a8)
print(mylist[4])


# access elements in a nested list
mylist = [[11,12],[21,22],[31,32]]
print(mylist)

a1 = mylist[1][0]
print(a1)


# modeling
# scenario
# two fighter jets in the battle area
# access elements in a 3 dimensional dataset



"""
ta:
    "9:20:15.456"
tb:
    "9:20:15.456"

Object 1.
    c11 = c(x11,y11,z11)
    t11 = ta
    
    c12 = c(x12,y12,z12)
    t12 = tb
   
Object 2.
    c21 = c(x21,y21,z21)
    t21 = ta
    
    c22 = c(x22,y22,z22)
    t22 = tb
"""

dataset_jets = [[('x11','y11','z11'),('x21','x22','x23')],[('x12','y12','z12'),('x22','y22','z22')]]
print(dataset_jets)

t0 = dataset_jets[0]
print("Location for jets, Time at 9:20:15.456:",t0)

p1 = t0[0]
print("Location of the fighter p1:",p1)

xp1 = p1[0]
print("The X coor of fighter p1: ", xp1)

# access
xp1 = dataset_jets[0][0][0]
print("x of p1 = ",xp1)

yp1 = dataset_jets[0][0][1]
print("y of p1 = ",yp1)

zp1 = dataset_jets[0][0][2]
print("z of p1 = ",zp1)








