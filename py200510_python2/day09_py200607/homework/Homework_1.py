import datetime
start = datetime.datetime.now()
my_list = [3, 8, 1, 6, 0, 8, 4]
target = 8
num = 0
for i in range(len(my_list)):
    if my_list[i] == target:
        if num == 0:
            num = 1
        else:
            print(i)

finish = datetime.datetime.now()
print(finish - start)

start = datetime.datetime.now()
my_list = [3, 8, 1, 6, 0, 8, 4]
target = 8
for i in range(len(my_list)):
    if my_list[i] == target:
        print(my_list.index(target, i+1))
        break
finish = datetime.datetime.now()
print(finish - start)