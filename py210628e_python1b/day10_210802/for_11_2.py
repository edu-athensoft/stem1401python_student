"""
find max and min at the same time
from a given number sequence
"""

# Andy

# data
num_list = [41, 21, 39, 32, 65, 35, 11, 14, 74, 45]

# get max and min
LENGTH = len(num_list)
# max = num_list[0]
# min = num_list[0]
max = min = num_list[0]

for index in range(LENGTH):
    current_num = num_list[index]
    if current_num > max:
        max = current_num
    if current_num < min:
        min = current_num

# for index in range(LENGTH):
#     current_num = num_list[index]
#     if current_num < min:
#         min = current_num

# output
print('The max and min number of the sequence: {} max is {}, min is {}'.format(num_list, max, min))
