"""
猜数字的AI v1
Guang Zhu Cui
2020-07-01
猜数字的AI
和猜数字一样，不过这次是设计一个能猜数字的AI
功能描述： 用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。
"""
from random import randint
print ('Please enter a number between 1-100 and the computer will guess the number.')
num = int(input("Enter a number for the computer to guess:"))
while num < 1 or num >100:
    if num > 100:
        print("Please enter a number less than or equal to 100")
    if num < 1:
        print("Please enter a number bigger than or equal to 1")
guess = randint(1, 100)
print ("The computer guessed...", guess)
times_guessed = 0
while guess != num:
    times_guessed += 1
    if guess > num:
        guess -= 1
        guess = randint(1, guess)
    else:
        guess += 1
        guess = randint(guess, 100)
    print("The computer guessed...", guess)
if guess == num:
    times_guessed += 1
    print("The computer guessed {} and it was correct!".format(guess))
print('The computer guessed {} times'.format(times_guessed))

