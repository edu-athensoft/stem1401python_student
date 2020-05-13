original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(original_list)

print(list(map(lambda a: a*a, filter(lambda a: a % 2 != 0, original_list))))