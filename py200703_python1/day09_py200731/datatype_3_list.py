"""
list slicing
"""

list1 = [2,3,4,5,6,7,8,9,10]

# case 1.   0..3
print("list1[0:3]=",list1[0:3])
print("list1[:3]=",list1[:3])

# case 1.   0..5
print("list1[0:5]=",list1[0:5])
print("list1[:5]=",list1[:5])


# case 2.   6..
last = len(list1)-1
print(last)
print("list1[6:8]=",list1[6:8])
print("list1[6:9]=",list1[6:9])
print("list1[6:9]=",list1[6:last+1])
print("list1[6:9]=",list1[6:len(list1)])
print("list1[6:]=",list1[6:])

# case 3.   n..m
# [5,6,7] expected

# lucas
print("=== Lucas ===")
print("list1[3:6]=",list1[3:6])

# xuanxuan
print(list1[3:6])

# jessica


# list is mutable (changeable)
print(list1)
list1[0] = 1
print(list1)

# add 11 to the list1
list1.append(11)
print(list1)

