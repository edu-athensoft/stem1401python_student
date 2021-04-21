"""
choice(name)
"""

import random

# choice()
mylist = ['White','Green','Blue','Golden','Orange']
# mylist = ('White','Green','Blue','Golden','Orange')

for i in range(10):
    a = random.choice(mylist)
    print(f"Chosed random item is {a}")
