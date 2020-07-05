"""
random
"""

import random

# randrange(start, stop) exclude stop number
# draw for 1 to 6
for i in range(10):
    print(random.randrange(1,7), end="\t")
print()
print()

for i in range(10):
    print(random.randint(1,6), end="\t")
print()
print()


# choice()
mylist = ['a','b','c','d','e']
a = random.choice(mylist)
print(a)

# write a program to prove the probability is close to set
role = 'WIZARD'
attr = ['BABARIAN','WIZARD','ARCHER','DOCTOR','MONK']
prob = 0.2

# draw once

# draw N times

# count how many times the target occurs

# analysis

# result








