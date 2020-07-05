my_list = [3, 8, 1, 6, 0, 8, 4]
target = 8
num = 0
for i in range(len(my_list)):
    if my_list[i] == target:
        if num == 0:
            num = 1
        else:
            print(i)

#
for i in range(len(my_list)):
    if my_list[i] == target:
        print(my_list.index(target, i+1))
        break


#
indexPosList = []
for i in range(len(my_list)):
    if my_list[i] == target:
        indexPosList.append(i)
print(indexPosList[1])




#
indexPosList = []
for i in range(len(my_list)):
    if my_list[i] == target:
        indexPosList.append(i)
print(indexPosList)