"""

find max and min at the same time
from a given number sequence

"""
# Kevin

numlist = [2, 3, 5, 6, 4, 7, 8, 5, 2, 3, 4, 2, 1]
LENGTH = len(numlist)
max = numlist[0]

# for index in range(LENGTH):
#     current_num = numlist[index]
#     print("numlist[{}] is {}".format(index, current_num))

min = numlist[0]
for index in range(LENGTH):
    current_num = numlist[index]
    print("numlist[{}] is {}".format(index, current_num))
    if current_num>max:
        max = current_num
    if current_num < min:
        min = current_num

print("The max number of the sequence: {} is {}".format(numlist, max))
print("The min number of the sequence: {} is {}".format(numlist, min))