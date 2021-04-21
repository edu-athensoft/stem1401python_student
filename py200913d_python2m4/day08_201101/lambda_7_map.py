"""
map()

mapping relationship
"""

my_list = [1,5,4,6,8,11,3,12]

# double every item in my_list
# get a new list named new_list

new_list = []

print(my_list)


# print(my_list *2)

for item in my_list:
    # print(item, item * 2)
    doubled = item * 2
    new_list.append(doubled)

# check the result
print(new_list)




# map()
# map(func, iter1)

result = map(lambda x : x * 2, my_list)
# print(result, type(result))

result2 = list(result)
# print(result2, type(result2))

print(result2)


# print out a mapped list
print(list(map(lambda x : x * 2, my_list)))
