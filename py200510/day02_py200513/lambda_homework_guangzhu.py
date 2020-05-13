original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(original_list)

# a = (filter(lambda x: x % 2 != 0, map(lambda x: x * x, original_list)))
a = filter(lambda x: x % 2 != 0, map(lambda x: x * x, original_list))
print(list(a))


# set blank line
# redundant () for line 4


