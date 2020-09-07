"""
random - treasure chest

"""

import random

# list of every drop
probability = []

# add 638 Normal to list
for i in range(638):
    probability.append("Normal")

# add 250 Magical to list
for i in range(250):
    probability.append("Magical")

# add 100 Rare to list
for i in range(100):
    probability.append("Rare")

# add 10 legendary to list
for i in range(10):
    probability.append("Legendary")

# add 2 Ancient Legendary to list
for i in range(2):
    probability.append("Ancient Legendary")

# number of drops dictionary
num_of_drops = {
    "Normal" : 0,
    "Magical" : 0,
    "Rare" : 0,
    "Legendary" : 0,
    "Ancient Legendary" : 0
}

# number of draws
draws = 10000

# random individual drop
for i in range(draws):
    random.shuffle(probability)
    num_of_drops[probability[0]] += 1
else:
    print("In {} draws, you got:".format(draws))

# print out answer
for rarity in num_of_drops:
    print("{} = {}".format(rarity,num_of_drops[rarity]))
