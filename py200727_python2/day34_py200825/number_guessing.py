import random

# title of the game
print("==Welcome to the game of fun==")

# menu
print("select your level of difficulty:")
difficulties = ["1. Beginner", "2. Intermediate", "3. Medium", "4. Hard", "5. Pro", "6. Mockery"]
num_guesses = [18,12,10,7,5,2]

for diff in difficulties:
    print(diff)

# selecting levels
difficulty = int(input("please enter the corresponding number: "))


# game settings for target number
answer = random.randint(1,101)

def user_inp_guess():
    guess = int(input("your guess?"))

print("The answer is a number from 1 to 100")

guess = int(input("your guess?"))

error_count = 0

while guess != answer:
    error_count += 1
    if error_count == num_guesses[difficulty-1]:
        print("You have used up all your guesses.")
        print("Game over! :(")
        print("The answer was {}".format(answer))
        break
    if guess > answer:
        print("Your answer is too big.")
    elif guess < answer:
        print("Your answer is too small.")
    print("You have {} remaining guesses.".format(num_guesses[difficulty-1] - error_count))
    guess = int(input("Your guess?  "))
else:
    print("Congratulations! You win! :)")