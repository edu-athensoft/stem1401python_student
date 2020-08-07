"""
stem1402_python_homework_8_steven
"""
import random

print("=== Reward Chances ===")
print("Normal - 63.8%")
print("Magic - 25%")
print("Rare - 10%")
print("Legendary - 1%")
print("Ancient legendary - 0.2%")
print()
print("-------------------------------------------------------------")

for i in range(5):
    chance = random.randint(1, 100)
    if chance <= 63.8:
            print("You got: Normal")

    elif chance <= 63.8+25:
            print("You got: Magic")

    elif chance <= 63.8+25+10:
            print("You got: Rare")

    elif chance <= 63.8+25+10+1:
            print("You got: Legendary")

    elif chance <= 63.8+25+10+1+0.2:
            print("You got: Ancient legendary")

