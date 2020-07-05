"""
break down into small problems
   1. find the max num.
   2. find the min num.
   3. combine the two logic
"""

list_num = [3,4,5,6,2,8,1,9,0,7]

# find the max
max = list_num[0]

for i in list_num:
    # print(i)
    # compare with the max num
    # if i > max
    # i -> max
    # otherwise, ignore and move on
    if i> max:
        max = i

print("The max num is {}".format(max))


#
min = list_num[0]

for i in list_num:
    # print(i)
    # compare with the max num
    # if i < min
    # i -> min
    # otherwise, ignore and move on
    if i < min:
        min = i

print("The min num is {}".format(min))