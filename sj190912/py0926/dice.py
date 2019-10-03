# dice 1,2,3,4,5,6

import random

# a = random.randint(1,6)
# print(a)

for i in range(0,100):
    a = random.randint(1,6)
    print(a, end=",")
    if((i+1)%10==0):
        print()

#

