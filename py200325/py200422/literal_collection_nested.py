"""
nested collection
"""

# list - nested list
my_list1 = [11,12,13,21,22,23,31,32,33]
print(my_list1)

my_list1 = [[11,12,13],[21,22,23],[31,32,33]]

my_list1 = [[11,12,13],
            [21,22,23],
            [31,32,33]]

print(my_list1)

# tuple - nested tuple
# 3x3
my_tuple1 = ((11,12,13),(21,22,23),(31,32,33))

# RPG role
# start point (10,10) -> (20,38) -> (40,50) -> (200,300) -> (60, 20) end point
# using nested tuple to represent the routine
routine = ((10,10),(20,38),(40,50),(200,300),(60, 20))
print(routine[0])
print(routine[1])
print(routine[2])
print(routine[3])
print(routine[4])

print("===")
print("x1 =",routine[0][0], "y1 = ",routine[0][1])
print("x2 =",routine[1][0], "y2 = ",routine[1][1])


# nested dictionary
my_dict1 = {1: 'a',  2: 'b'}
my_dict2 = {3: 'c',  4: 'd', 5 : my_dict1}
print(my_dict2)


# set
# my_set1 = {1,2,3,{4,5,6}}
# print(my_set1)