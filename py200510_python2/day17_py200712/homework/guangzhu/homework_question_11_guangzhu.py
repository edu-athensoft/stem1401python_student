dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
a = dict1.values()
list1 = list(a)

# rewrite this
b = list1[0] * list1[1] * list1[2] * list1[3]

print(b)
