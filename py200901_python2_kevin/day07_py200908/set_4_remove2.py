"""
remove an item from a set
pop() - randomly remove an item and return it
"""

my_set = {'1', '3', '4', '5', '6'}

for i in range(len(my_set)):
    delitem = my_set.pop()
    print(delitem)

