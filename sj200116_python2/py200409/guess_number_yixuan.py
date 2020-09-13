"""
app: number guessing game
version: 2.1
author: Yixuan Wang
"""
import random
def compare(x,s):
      if x > s:
          print("Too big")
      elif x < s:
          print("Too small")
      else:
          print("Bingo")
s = random.randrange(1,101)
print("r1 randint = {}".format(s))
print("Welcome to my game Guess_Number")
print("Level 1: Easy 40 to 50 Chance")
print("Level 2: Medium 30 to 20 Chance")
print("Level 3: Difficulty 10 to 1 Chance")
choose = str(input("Please choose game level:"))
if choose == '1':
    z = int(input("how many tries do you want 60 to 50: "))
    for i in range(1):
        if z > 60 or z < 50:
            print("is not exist")
            break
        elif z > 50 or z < 60:
            pass
        else:
            break
        for a in range(z):
            x = float(input("Guess a natural number between 1 and 100: "))
            # s = 69
            isBingo = compare(x, s)
            if isBingo:
                break
            elif x > 100 or x < 1:
                print("Warning: Please input a valid number!")
                break
            elif x == s:
                break
            else:
                z = z - 1
                print("You have only {} chance(s) left! ".format(z))
                # print("r1 randint = {}".format(s))
elif choose == '2':
    z = int(input("how many tries do you want 40 to 30: "))
    for i in range(1):
        if z > 40 or z < 30:
            print("is not exist")
            break
        else:
            pass
        for a in range(z):
            x = float(input("Guess a natural number between 1 and 100: "))
            # s = 69
            isBingo = compare(x, s)
            if isBingo:
                break
            elif x == s:
                break
            else:
                z = z - 1
                print("You have only {} chance(s) left! ".format(z))
                # print("r1 randint = {}".format(s))
elif choose == '3':
    z = int(input("how many tries do you want 10 to 1: "))
    for i in range(1):
        if z > 10 or z < 1:
            print("is not exist")
            break
        else:
            pass
        for a in range(z):
            x = float(input("Guess a natural number between 1 and 100: "))
            # s = 69
            isBingo = compare(x, s)
            if isBingo:
                break
            elif x == s:
                break
            else:
                z = z - 1
                print("You have only {} chance(s) left! ".format(z))
                # print("r1 randint = {}".format(s))
elif choose > '4' :
    print("Is not exite")
print("Game over")