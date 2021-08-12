"""
[Challenge] Find the min number

assuming max number comes from a number sequence


"""

# from Kevin
numlist = [3,5,4,7,2,8,1,7,5,6,9]
LENGTH = len(numlist)

min = numlist[0]

for index in range(LENGTH):
    current_num = numlist[index]
    # print("numlist[{}] is {}".format(index, current_num))

    if current_num < min:
        min = current_num

print("The min number of the sequence: {} is {}".format(numlist, min))