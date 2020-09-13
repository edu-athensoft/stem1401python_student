"""

"""

"""
app: Guessing Number Game
By: Leon Li
"""
import random
answer1 = random.randrange(1, 101)
def compare(x, answer):
    flag = False
    if x > answer:
        print("Too big")
    elif x < answer:
        print("Too small")
    else:
        print("Bingo!")
        flag = True
    return flag
def validate():
    x = ''
    while True:
        x = int(input("Guess a number (1-100):"))
        if x > 100 or x < 1:
            print("Warning: Please input a valid number!")
        else:
            break
    return x
def set_difficulty():
    print("1. Noob")
    print("2. Easy")
    print("3. Medium")
    print("4. Hard")
    print("5. Nightmare")
    print("6. Impossible")
    chances = 0
    choice = input("Choose the difficulty (1 - 6): ")
    if choice == "1":
        chances = 25
    elif choice == "2":
        chances = 15
    elif choice == "3":
        chances = 10
    elif choice == "4":
        chances = 5
    elif choice == "5":
        chances = 3
    elif choice == "6":
        chances = 2
    return chances
a = set_difficulty()
print("You have {} chances to guess the number".format(a))
for i in range(a):
    x = validate()
    isBingo = compare(x, answer1)
    if isBingo:
        print("You win!")
        break
    else:
        i = i - 1
        print("You have {} chances left.".format(a - i - 2))
else:
    print("You lose!")