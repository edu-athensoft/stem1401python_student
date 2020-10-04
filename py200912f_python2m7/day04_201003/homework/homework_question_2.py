"""
2. Write a program to sort a dictionary by key in both ascending and descending order.
"""

# ascending

my_dict = {1: "a", 5: "c", 4: "x", 9: "y"}
print(sorted(my_dict))

# descending

my_dict_2 = {2: "a", 8: "c", 5: "x", 9: "y"}
print(sorted(my_dict, reverse=True))


# solution
# sorted(), dict.items()
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)


res1 = sorted(my_dict)
print(res1, type(res1))

for key in res1:
    print(f"{key} : {my_dict[key]}")
