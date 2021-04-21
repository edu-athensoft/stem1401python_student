"""
from 1 to 100 number sequence
get square of every even number in the sequence

2,4,.....,100
expected result: 4,16,....,10000


hints:
map(), filter()

solution 1.
do filtering first,  then do mapping


algorithm
1+....+100

a1.  for-loop
a2.  recursive function
a3.  math formula:   (1+100)100/2

performance
1. spacial
2. time
"""


# step1.
my_list = list(range(1,101))
filtered_list = list(filter(lambda x : x%2 ==0, my_list))

# print(filtered_list)

# step2.
result = list(map(lambda i: i**2, filtered_list))

print(result)