"""
Number guessing AI v1.1
Ze Yue Li
2020-06-27
猜数字的AI
和猜数字一样，不过这次是设计一个能猜数字的AI
功能描述： 用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。
"""


def input_num(message, smallerthan=-1, greaterthan=0):
    num = input(message)
    while not num.isdigit():
        num = input(message)
    while int(num) < greaterthan or int(num) > smallerthan > -1:
        num = input(message)
        while not num.isdigit():
            num = input(message)
    return num


def possible_nums(num_range):
    pos_nums = []
    for i in range(num_range[0], num_range[1] + 1):
        pos_nums.append(i)
    return pos_nums

def guess(pos_nums, num_to_guess):
    guess = pos_nums[len(pos_nums) // 2]
    guesses = 1
    while guess != num_to_guess:
        guesses += 1
        if guess > num_to_guess:
            pos_nums2 = pos_nums.copy()
            pos_nums.clear()
            for i in range(pos_nums2[0], guess):
                pos_nums.append(i)
        else:
            pos_nums2 = pos_nums.copy()
            pos_nums.clear()
            for i in range(guess + 1, pos_nums2[-1] + 1):
                pos_nums.append(i)
        guess = pos_nums[len(pos_nums) // 2]
    print(guess)
    print('The AI guessed {} times'.format(guesses))


num_to_guess = int(input_num('Input an integer for the computer to guess:'))
num_range_start = input_num("Input the first number of a range covering your number:", num_to_guess)
num_range_end = input_num("Input the second number of the range", -1, num_to_guess)
num_range = [int(num_range_start), int(num_range_end)]
pos_nums = possible_nums(num_range)
guess(pos_nums, num_to_guess)
