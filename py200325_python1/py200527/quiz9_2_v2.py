"""
break down into small problems
   1. find the max num.
   2. find the min num.
   3. combine the two logic

v2
"""
# prepare data
list_num = [3,4,5,6,2,8,1,9,0,7]


max = list_num[0]
min = list_num[0]

# processing
for i in list_num:
    if i> max:
        max = i

    if i < min:
        min = i


# output
print("The max num is {}".format(max))
print("The min num is {}".format(min))