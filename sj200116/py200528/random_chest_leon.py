"""
# how to prove the choice() function is a fair method
# A fair method means by using choice(), you can get 20% of chances to get items right for your class

# 写一个程序证明：choice（）对于开宝箱来说是公平的
#
"""

import random

item_class = ["WARRIOR", 'WIZARD', 'DOCTOR', 'ARCHER', 'MONK']
role = 'WIZARD'
CHANCES = 3000000

list_b = []
list_w = []
list_d = []
list_a = []
list_m = []

for i in range(CHANCES):
    current = random.choice(item_class)

    if current == "WARRIOR":
        list_b.append(current)
    elif current == 'WIZARD':
        list_w.append(current)
    elif current == 'DOCTOR':
        list_d.append(current)
    elif current == 'ARCHER':
        list_a.append(current)
    elif current == 'MONK':
        list_m.append(current)
    else:
        pass

print("Number of items for every class")
print("{} items in the list of WARRIOR, p is {:.2%}".format(len(list_b), len(list_b)/CHANCES))
print("{} items in the list of WIZARD, p is {:.2%}".format(len(list_w), len(list_w)/CHANCES))
print("{} items in the list of DOCTOR, p is {:.2%}".format(len(list_d), len(list_d)/CHANCES))
print("{} items in the list of ARCHER, p is {:.2%}".format(len(list_a), len(list_a)/CHANCES))
print("{} items in the list of MONK, p is {:.2%}".format(len(list_m), len(list_m)/CHANCES))
