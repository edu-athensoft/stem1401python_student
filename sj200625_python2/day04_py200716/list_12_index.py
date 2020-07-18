"""
index
find all specified items in a list
"""

mylist = [3, 8, 1, 6, 0, 8, 4, 3, 8, 1, 6, 0, 8, 4]
target_num = 8

# find all index of the target number

# for-loop
# list

# result:  [1,5,8,12]

result = []

# print(len(mylist))

for i in range(len(mylist)):
    if mylist[i] == target_num:
        print("list[{1}] = {0}".format(mylist[i], i))
        result.append(i)

print("result = {}".format(result))



