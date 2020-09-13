def replaceall(target, new):
    my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm'] * 3
    next_index = -1
    for i in my_list:
        if i == target:
            next_index = my_list.index(i, next_index + 1)
            print(next_index)
            my_list[next_index] = new
    return my_list


my_list = replaceall('r', 'x')
print(my_list)
