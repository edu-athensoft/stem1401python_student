"""
1. Write a program to simulate a treasure chest in video games
Design and write a program for a treasure chest in an MMORPG game.
The rank of items which may drop from the chest includes:
	normal						0.638
	magic				1/4		0.25
	rare				1/10	0.1
	legendary			1/100	0.01
	ancient legendary	1/500	0.002
Please write some test code to simulate opening chest for a couple of times (like 100 times), 500 times, 1000 times or more
Analyze the result with your settings of probability of items dropping from the chests.

"""


import random

treasure = ["normal item","magic item","rare item","legendary item","ancient legendary item"]

for i in range(1000):
    a = treasure.append(random.choice(treasure))
    print(f"Congratulation, you got a {a}")


f1 = [63.8/100]
f2 = [25/100]
f3 = [10/100]
f4 = [1/100]
f5 = [0.2/100]


for item in treasure:
    if item == "normal item":
        f1.append(item)
    if item == "magic item":
        f2.append("item")
    if item == "rare item":
        f3.append("item")
    if item == "legendary item":
        f4.append(item)
    if item == "ancient legendary item":
        f5.append(item)


num1 = len(f1)
print(1, num1/1000)
num2 = len(f2)
print(2, num2/1000)
num3 = len(f3)
print(3, num3/1000)
num4 = len(f4)
print(4, num4/1000)
num5 = len(f5)
print(5, num5/1000)






