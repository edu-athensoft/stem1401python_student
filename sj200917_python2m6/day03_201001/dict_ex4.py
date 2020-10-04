
mydict = {1: 2, 3: 4, 5: 3, 4: 3, 2: 1, 0: 0}
result = mydict.items()

key = lambda item:item[1]

# sorted(iterable, key, reverse)

sorted_result = sorted(result, key=lambda item:item[1], reverse=True)
sorted_dict = dict(sorted_result)

print(sorted_dict)