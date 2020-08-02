"""
number of items with more than 2 characters and starts and ends with same character
"""
list1 = ("abc", "xyz", "aba", "1221")
list2 = []
list3 = []

for i in list1:
    if len(i) >= 2 and i[0] == i[-1]:
        list2.append(i)

print(list2)
# print(len(list3))

