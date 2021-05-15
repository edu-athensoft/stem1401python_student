"""
homework: how to prove there is evenly distributed probability of 1-6 with a huge number of trials

f = 1/T

expectation: evenly distributed
"""


import random

for n in range(10000):
    res1 = random.randrange(1,7)
    # print(res1)
#
# ====================


# dict
frequencies = {}

res1 = str(res1)

for digits in res1:
    if digits in frequencies == "1":
        frequencies[digits] += 1
    else:
        frequencies[digits] = 1

print("The frequency of '{}' is :{}".format(res1,frequencies))

for digits in res1:
    if digits in frequencies == "2":
        frequencies[digits] += 1
    else:
        frequencies[digits] = 1

print("The frequency of '{}' is :{}".format(res1,frequencies))

for digits in res1:
    if digits in frequencies == "3":
        frequencies[digits] += 1
    else:
        frequencies[digits] = 1

print("The frequency of '{}' is :{}".format(res1,frequencies))

for digits in res1:
    if digits in frequencies == "4":
        frequencies[digits] += 1
    else:
        frequencies[digits] = 1

print("The frequency of '{}' is :{}".format(res1,frequencies))

for digits in res1:
    if digits in frequencies == "5":
        frequencies[digits] += 1
    else:
        frequencies[digits] = 1

print("The frequency of '{}' is :{}".format(res1,frequencies))

for digits in res1:
    if digits in frequencies == "6":
        frequencies[digits] += 1
    else:
        frequencies[digits] = 1

print("The frequency of '{}' is :{}".format(res1,frequencies))









