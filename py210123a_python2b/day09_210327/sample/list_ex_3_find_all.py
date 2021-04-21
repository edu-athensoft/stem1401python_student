"""
get all index of an item in a list
using range()
"""

def get_index3(lst=None, item=''):
    return [i for i in range(len(lst)) if lst[i] == item]


lst = ['A', 1, 4, 2, 'A', 3]

print(get_index3(lst, 'A'))

