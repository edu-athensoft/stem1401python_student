"""
from 1 to 100 number sequence
get square of every number in the sequence

1,2,3,.....,100
expected result: 1,4,9,16,....,10000
"""

# test
# for my_list in range(1,101):
#     print(my_list)

# step1. generate source list - my_list
my_list = list(range(1,101))
print(my_list, type(my_list))

# step2.
new_list = []

for item in my_list:
    square = item ** 2
    new_list.append(square)

print(new_list)



# solution 2. lambda function
result = list(map(lambda i: i**2, my_list))

print(result)