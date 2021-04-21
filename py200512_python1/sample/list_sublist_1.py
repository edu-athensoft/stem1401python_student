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

orglist = [1, 2, 3, 1, 7, 8, 2, 3, 14, 7, 8, 9]
targetlist = [2, 3, 14, 7]


def find_sublist(org_list, target_list):
    start_pos = org_list.index(target_list[0])
    offset_pos = 0
    issublist = True

    for ti in target_list:
        current_pos = start_pos+offset_pos
        if ti == org_list[current_pos]:
            offset_pos += 1
            continue
        else:
            issublist = False
            break

    return issublist

# test ok
# print(find_sublist(orglist, targetlist))

current_pos = 0
last_pos = len(orglist) - 1
next_pos = 0


# while current_pos <= last_pos and next_pos <= last_pos:
#     next_pos = orglist.index(targetlist[0], current_pos, last_pos)
#     print(next_pos)
#     current_pos = next_pos + 1

list1 = [1,2,3]
print(list1.index(4))


