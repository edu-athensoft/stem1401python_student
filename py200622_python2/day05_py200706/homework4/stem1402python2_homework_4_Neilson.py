"""
Homework 4
print the fibonacci sequence
"""

fibonacci_number = int(input(""))


def fibonacci_pos_finder(x):
    count = 3
    item_1 = 1
    item_2 = 1
    result = item_1 + item_2
    if x == 1:
        return 1
    elif x == 2:
        return 2
    while True:
        if count == x:
            return result
        else:
            item_1 = item_2
            item_2 = result
            result = item_1 + item_2
            count += 1


print(fibonacci_pos_finder(fibonacci_number))
