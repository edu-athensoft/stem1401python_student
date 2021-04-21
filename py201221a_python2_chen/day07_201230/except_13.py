"""
Write a small game

A user guess the number within a range (0,100)

user can input one number at a time

if the number is larger than the result,
  then print out 'too large'
else if the number is smaller then the result,
  then print out 'too small'

till the user bingo!

Binary search method

"""


from random import randint

# step 1. to generate a target number to guess
target = randint(0, 100)

# step 2. to receive a user's input
while True:
    guess = input('please guess an Integer between 0 and 100:')

    try:
        num = int(guess)
    except ValueError as ve:
        print("Please input an INTEGER!!")
    else:
        break


# step 3. comparison
while num != target:
    if num < target:
        print("too small")
    elif num > target:
        print("too large")

    while True:
        guess = input('guess again')
        try:
            num = int(guess)
        except ValueError as ve:
            print("Please input an INTEGER!!")
        else:
            break
    else:
        print(f'You win ! and the number is {target}')

