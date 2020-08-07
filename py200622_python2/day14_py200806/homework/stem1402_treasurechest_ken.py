"""
For August 6th, 2020.
Ken
Treasure Chest
"""

"""
Drop chances

	normal						0.638
	magic				1/4		0.25
	rare				1/10		0.1
	legendary			1/100		0.01
	ancient legendary		1/500		0.002
"""


import random as r


def dropper(drop_number):

    if drop_number <= 638:
        return "normal"
    elif drop_number <= 888:
        return "magic"
    elif drop_number <= 988:
        return "rare"
    elif drop_number <= 998:
        return "legendary"
    elif drop_number <= 1000:
        return "ancient legendary"


print("---Treasure Chest---")

n = 1
while n <= 100:
    print(f"Try #{n}")
    drop_number = r.randint(1,1000)
    print(f"Your drop is {dropper(drop_number)}")
    n += 1