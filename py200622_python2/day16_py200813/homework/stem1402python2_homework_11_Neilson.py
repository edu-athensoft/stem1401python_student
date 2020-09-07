"""
Homework 11
"""

# Question 1

sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def sorter(x):
    for i in range(len(x) - 1, 0, -1):
        for j in range(i):
            if x[j][-1] > x[j + 1][-1]:
                x[j], x[j + 1] = x[j + 1], x[j]
    return x


print(sorter(sample_list))

# Question 2

list_1 = [1, 3, 2, 5, 3, 1, 2, 5, 7, 3]


def duplicates(x):
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] == x[j]:
                x[j] = " "

    x = list(filter(lambda x: x != " ", x))
    return x


print(duplicates(list_1))

# Question 3

list_2_1 = []
list_2_2 = [1, 2, 4, 2]


def list_checker(x):
    if not x:
        return "This like is empty"
    else:
        return "This list is not empty"


print(list_checker(list_2_1))
print(list_checker(list_2_2))

# Question 4

list_3 = [1, 4, 5, 2, 4, 5, 1, 7, 6]


def copy(x):
    list_4 = x.copy()
    return list_4


print(f"List_3 = {list_3} and List_4 = {copy(list_3)}")

# Question 5

str_1 = "The quick brown fox jumps over the lazy dog"


def work_checker(x):
    list_5 = x.split()
    list_6 = []

    for i in list_5:
        if len(i) > 3:
            list_6.append(i)
    return list_6


print(work_checker(str_1))
