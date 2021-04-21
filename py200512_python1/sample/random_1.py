"""
module: random
"""

# import math

import random

# get a random number from a specified range
# start, stop
# randrange(start, stop), and the stop number is excluded
for i in range(100):
    print(random.randrange(1,6), end=",")
print()

# randint(start, stop)
for i in range(100):
    print(random.randint(1,6), end=",")

