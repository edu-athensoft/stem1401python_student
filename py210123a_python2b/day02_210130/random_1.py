"""
module: random
"""


import random

# randrange(N)
# res1 = random.randrange(6)
# print(res1)
#
# res1 = random.randrange(6)
# print(res1)


for n in range(10):
    res1 = random.randrange(6)
    print(res1)
print('======')


# randrange(a, b)
for n in range(20):
    res1 = random.randrange(1,7)
    print(res1)
print('======')

"""
Date: 2021-01-30
How to prove there is evenly distributed probability of 1-6 with a huge number of trials
Due Date: by the end of next Friday
"""



# randint
# res2 = random.randint(1,6)
# print(res2)

for n in range(20):
    res1 = random.randint(1,7)
    print(res1)
print('>>>>>>>')

for n in range(20):
    res1 = random.randint(9)
    print(res1)
print('======')


