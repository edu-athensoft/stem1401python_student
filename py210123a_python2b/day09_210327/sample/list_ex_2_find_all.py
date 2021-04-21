"""
get all index of an item in a list
"""


def get_index1(lst=None, item=''):
    return [index for (index,value) in enumerate(lst) if value == item]


lst = ['A', 1, 4, 2, 'A', 3]
print(get_index1(lst, 'A'))
