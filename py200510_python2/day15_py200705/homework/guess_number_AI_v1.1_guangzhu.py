"""
猜数字的AI v1.1
Guang Zhu Cui
2020-07-01
猜数字的AI
和猜数字一样，不过这次是设计一个能猜数字的AI
功能描述： 用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。
"""

from random import randint


def computer_guess(num):
    global times_guessed
    times_guessed = 0
    num_range_first_number = int(input('Please enter the first number of a range covering your number:'))
    num_range_last_number = int(input('Please enter the last number of a range covering your number:'))
    guess = randint(num_range_first_number, num_range_last_number)
    while guess != num:
        print("The computer guessed...", guess)
        times_guessed += 1
        if guess > num:
            num_range_last_number = guess
        elif guess < num:
            num_range_first_number = guess + 1
        guess = (num_range_first_number + num_range_last_number) // 2
    print("The computer guessed {} and it was correct!".format(guess))
    times_guessed += 1


def main():
    num = int(input("Enter a number you want the computer to guess:"))
    computer_guess(num)


main()
print('The computer guessed {} times'.format(times_guessed))
