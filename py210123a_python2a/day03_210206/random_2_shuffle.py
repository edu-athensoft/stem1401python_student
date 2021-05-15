"""
shuffle()
"""

import random

# shuffle(x)
mylist = ['White','Green','Blue','Golden','Orange']

# a = random.shuffle(mylist)
# print(a, type(a))

for i in range(5):
    random.shuffle(mylist)
    print(mylist)


#  example
treasure = ['coin','coin','coin','coin','exp','exp','exp','weapon','weapon','gem']
random.shuffle(treasure)

for i in range(100):
    print(random.choice(treasure))