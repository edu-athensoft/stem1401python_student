"""
Number guessing AI v1.0
Ze Yue Li
2020-06-27
猜数字的AI
和猜数字一样，不过这次是设计一个能猜数字的AI
功能描述： 用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。
"""

num = int(input('Input a number'))
num_range = [int(input("Input the first number of a range covering your number")), int(input('Input the second number of the range'))]
pos_nums = []
for i in range(num_range[0], num_range[1]+1):
    pos_nums.append(i)
guess = pos_nums[len(pos_nums) // 2]
guesses = 1
while guess != num:
    guesses += 1
    if guess > num:
        pos_nums2 = pos_nums.copy()
        pos_nums.clear()
        for i in range(pos_nums2[0], guess):
            pos_nums.append(i)
    else:
        pos_nums2 = pos_nums.copy()
        pos_nums.clear()
        for i in range(guess+1, pos_nums2[-1]+1):
            pos_nums.append(i)
    guess = pos_nums[len(pos_nums)//2]
print(guess)
print('The AI guessed {} times'.format(guesses))