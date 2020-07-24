my_dict = {1: 4, 5: 3, 7: 9}


def sort_by_value(my_dict_1):
    items = my_dict_1.items()
    back_items = [[v[1], v[0]] for v in items]
    back_items = sorted(back_items)
    print([back_items[i][1] for i in range(0, len(back_items))])
    print([v for v in sorted(my_dict_1.values())])


sort_by_value(my_dict)

