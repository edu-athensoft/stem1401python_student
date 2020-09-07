"""
Project name:     Guess the number game
Version:
Author :          Kevin
Created date:           2020-08-24
Last modified date:     2020-08-24
"""
import random


# echo number of choices you have
def echoguesscount():
    print("You have {} guesses.".format(num_guesses[diff-1]-fails))

# check if guess if correct
def checkanswer(guess, answer):
    if guess > answer:
        print("Your guess is too big.")  # comparison
        print("You have {} remaining guess.".format(limit - fails))  # echo remaining guess
    elif guess < answer:
        print("Your guess is too small.")  # comparison
        print("You have {} remaining guess.".format(limit - fails))  # echo remaining guess

# user guess
def askinput():
    guess = int(input("Your guess? "))
    return guess


# title
print("===Welcome to Guess the Number!===")


"""
game settings
"""
# generate a number for answer
answer = random.randrange(1, 101)

# difficulties
difficulties = ["1. Beginner","2. Intermediate","3. Medium","4. Hard","5. Pro","6. Impossible"]
# number of guesses
num_guesses = [20,10,8,6,3,2]


"""
main program
"""
# print menu
for diff in difficulties:
    print(diff)

# choice of difficulty
diff = int(input("Choose your difficulty: "))
# limit of guesses
limit = num_guesses[diff-1]

# rules explanation
print("The answer is a random number from 1 and 100.")

# initial amount of guesses
echoguesscount()

# fail count
fails = 0
guess = 0

# while loop
while guess != answer:
    guess = askinput()
    fails += 1
    checkanswer(guess, answer)
    if fails == limit:
        print("Game Over!")
        print("The answer was {}.".format(answer))
        break
else:
    print("Bingo")
