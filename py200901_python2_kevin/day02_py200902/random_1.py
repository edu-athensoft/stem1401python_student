"""
there are many random cases or numbers in the nature

to generate a real random number is not easy

random seed
random number

random event

evenly distributed
weighed distributed -> not evenly distributed
"""

import random

# to create random
a = random.randrange(6)
print(a)

# write a program to prove the number you input is not included in the random number set.
# while True:
#     a = random.randrange(6)
#     if a == 6:
#         print(a)
#         break

a = random.randrange(1,7)
print(a)
print()

# experiments 100, 1000, 10000
for i in range(10):
    a = random.randrange(1,7)
    print(a)


b = random.randint(1,6)
print()

for i in range(100):
    b = random.randint(1,6)
    print(b)

