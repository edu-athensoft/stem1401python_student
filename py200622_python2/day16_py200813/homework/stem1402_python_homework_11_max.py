"""
Homework 11
"""

# 1.

# ?
# Tuples are immutable

# 2.
mylist = [1, 1, 5, 4, 2, 6, 9, 7, 5, 4, 6]


def duplicate(num_list):
    for i in num_list:
        count = num_list.count(i)

        for x in range(count - 1):
            num_list.remove(i)

    return num_list


print(duplicate(mylist))

# 3.
mylist = []
mylist2 = [1]


def empty_check(list):
    if len(list) < 1:
        return True
    else:
        return False


print(empty_check(mylist))
print(empty_check(mylist2))

# 4.
mylist = [1, 2, 3, 4, 5, 6]
mylist2 = []


def clone(list1, list2):
    for i in list1:
        list2.append(i)

    return list2


print(clone(mylist, mylist2))

# 5.
words = 'The quick brown fox jumps over the lazy dog'
words = words.split()

def length_check(list):
    word_list = []

    for i in list:
        if len(i) > 3:
            word_list.append(i)

    return word_list


print(length_check(words))
