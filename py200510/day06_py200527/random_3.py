"""
random
"""

import random


# shuffle()
# ordered -> unordered
# operate on the original data object
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
for i in range(10):
    random.shuffle(list1)
    print(list1)

# scenario
spawn_locations = ['zone1', 'zone2', 'zone3', 'zone4']
for i in range(10):
    random.shuffle(spawn_locations)
    print(spawn_locations)



