"""
to get an item from a list(sequence) randomly

write a program to open the treasure box for rewarding system
each time the player can get ONE item

"""
import random

items = ['gold','weapon','diamond','pet','armor','hp portion','mp portion']
#
# a = random.randrange(6)
# print(a)


for i in range(30):
    random1 = random.randrange(7)
    # print(random1)
    print("you got",items[random1],"!")


