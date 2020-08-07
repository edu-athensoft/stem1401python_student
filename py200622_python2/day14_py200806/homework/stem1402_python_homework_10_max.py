"""
Homework 10
"""

import random



normal = 0
magic = 0
rare = 0
legendary = 0
ancient_legendary = 0

for i in range(1000):

    chance = random.randint(1, 1000)

    if chance in range(1, 638):
        print('normal')
        normal += 1
    elif chance in range(639, 888):
        print('magic')
        magic += 1
    elif chance in range(889, 988):
        print('rare')
        rare += 1
    elif chance in range(989, 998):
        print('legendary')
        legendary += 1
    elif chance in range(999, 1000):
        print('ancient legendary')
        ancient_legendary += 1

print(f'normal: {normal}, magic: {magic}, rare: {rare}, legendary: {legendary}, ancient legendary: {ancient_legendary}')














