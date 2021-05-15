"""
count()
returns the count of number of items passed as an argument
"""

odd = [1,2,10,31,5,10,7,9,10,12,14,10]

value = 10

num_value = odd.count(value)
print(num_value)


# how to remove all items of 10 from odd
for i in range(num_value):
    odd.remove(value)

print(odd)




