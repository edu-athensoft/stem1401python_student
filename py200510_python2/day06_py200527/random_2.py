"""
random
"""

import random

chest = ['weapon', 'portion', 'pet', 'armor', 'ring']

# choice()
# for i in range(100):
#     print(random.choice(chest))

# option 1. counters for each class of item
# 5 counters

# option 2. grouping
# 5 containers using list
list_weapon = []
list_portion = []
list_pet = []
list_armor = []
list_ring = []
list_exception = []

# the times of event
N = 1000000

for i in range(N):
    current_item = random.choice(chest)
    if current_item == 'weapon':
        list_weapon.append(current_item)
    elif current_item == 'portion':
        list_portion.append(current_item)
    elif current_item == 'pet':
        list_pet.append(current_item)
    elif current_item == 'armor':
        list_armor.append(current_item)
    elif current_item == 'ring':
        list_ring.append(current_item)
    else:
        list_exception.append(current_item)

# len()
print("There are {} weapon(s), \tp= {:.1%}".format(len(list_weapon), len(list_weapon)/N))
print("There are {} portion(s), \tp= {:.1%}".format(len(list_portion), len(list_portion)/N))
print("There are {} pet(s), \t\tp= {:.1%}".format(len(list_pet), len(list_pet)/N))
print("There are {} armor(s), \t\tp= {:.1%}".format(len(list_armor), len(list_armor)/N))
print("There are {} ring(s), \t\tp= {:.1%}".format(len(list_ring), len(list_ring)/N))
print("There are {} exception(s), \tp= {:.1%}".format(len(list_exception), len(list_exception)/N))




