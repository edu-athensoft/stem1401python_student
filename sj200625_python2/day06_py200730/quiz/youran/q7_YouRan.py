"""
remove duplicates
"""
list1 = [1, 1, 1, 1, 3, 3, 4, 4, 5, 6, 7]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    # else:
    #     pass
print(list2)
