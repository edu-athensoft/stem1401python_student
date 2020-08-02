"""
sort by biggest second number
"""
list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list1.sort(key=lambda i: i[1])
print(list1)
