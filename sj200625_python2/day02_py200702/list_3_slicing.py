"""
list slicing
"""

mylist = [1,2,3,4,5,6,7,8,9]


# case 1. slicing from the most left
res = mylist[0:5]
print("mylist[0:5]",res)

# 1..5
x = mylist[:5]
print("mylist[:5]",x)

# ex. slicing for 1..8
# leon
# x = mylist[0:7}
# Print(x)
x = mylist[0:8]
print(x)






# youran
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = my_list[0:8]
print(result)


# chengjun
res =mylist[0:8]
print(res)


# case 2. slicing from the(any) middle to the end
# from 5..9
res = mylist[4:9]
print("mylist[4:9]",res)

res = mylist[4:len(mylist)]
print("mylist[4:len(mylist)]",res)

res = mylist[4:]
print("mylist[4:]",res)

# res = mylist[4:-1]
# print(res)

# res = mylist[4:0]
# print(res)

# youran
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
middle = round(len(my_list)/2)
result = my_list[middle:len(my_list)]
print(result)


# case 3. slicing
res = mylist[2:7]
print(res)

# ex. slicing for 4..6
# youran
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = my_list[3:6]
print(result)

# leon
x = mylist[3:6]
print(x)

# chengjun
res= mylist[3:6]
print(res)


# slicing for all items
res = mylist[:]
print("mylist[:]",res)
print("mylist ",mylist)







