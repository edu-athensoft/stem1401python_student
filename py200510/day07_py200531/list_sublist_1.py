"""

"""

# option 2.
list_2 = [1, 2, 3, 14, 7, 8]
# list_3 = [1, 2, 3, 14, 7]
list_3 = [2, 3, 14, 7]

# a = False
# for i in range(len(list_2)-(len(list_3)-1)):
#     for j in range(len(list_3)):
#         if not list_2[i+j] == list_3[j]:
#             break
#         if j == len(list_3)-1:
#             a = True
# print(a)


# option 2.
# list_2 = [1, 2, 3, 14, 7, 8]
# list_3 = [2, 3, 14, 7]

org_list = [1, 2, 3, 1, 7, 8, 2, 3, 14, 7, 8, 9]
target_list = [2, 3, 14, 7]

start_pos = org_list.index(target_list[0])
print("start_pos",start_pos)
for ti in target_list:
    print(ti)


