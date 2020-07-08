"""
Python dictionary
Sorting by value

references:
https://blog.csdn.net/buster2014/article/details/50939892
"""

def sort_by_value(mydict):
    """

    :param mydict:
    :return: sorted dict by value, displaying key
    """
    items = mydict.items()
    backitems = [[v[1],v[0]] for v in items]
    # backitems.sort()
    backitems = sorted(backitems)
    return [ backitems[i][1] for i in range(0,len(backitems))]


def sort_by_value2(mydict):
    return [v for v in sorted(mydict.values())]


def sort_by_value3(mydict):
    return sorted(mydict.items(), key=lambda item: item[1])


# main program
demo_dict = {
    1: "c",
    2: "a",
    3: "b"
}
print("Original dictionary is: {}".format(demo_dict))
print()

# test 1
print("[info] testing sort_by_value()")
print(sort_by_value(demo_dict))
print()

# test 2
print("[info] testing sort_by_value2()")
print(sort_by_value2(demo_dict))
print()

# test 3
print("[info] testing sort_by_value3()")
print(sort_by_value3(demo_dict))
print()

