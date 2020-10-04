"""
3. Write a program to sort a dictionary by value in both ascending and descending order.
"""

import operator

# ascending

my_dict = {1: "a", 5: "c", 4: "x", 9: "y"}
a = sorted(my_dict.items(), key=operator.itemgetter(1))
print(dict(a))

# descending

my_dict_2 = {1: "a", 8: "c", 3: "x", 5: "y"}
b = sorted(my_dict_2.items(), key=operator.itemgetter(1), reverse=True)
print(dict(b))


# solution 2. using lambda function
f = lambda item : item[1]
b = sorted(my_dict.items(), key=f)
print(dict(b))

#
b = sorted(my_dict.items(), key=lambda item : item[1])
print(dict(b))

# f = lambda x:  2*x
# f2 = lambda y: y[1]
