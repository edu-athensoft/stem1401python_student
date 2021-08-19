"""
application of continue

print out all even numbers
"""


mylist = [33,67,34,7,3,8,2,5,8,58,34,21,66,67]


# for num in mylist:
#     if num % 2 == 0:
#         print(num)


for num in mylist:
    if num % 2 == 1:
        continue

    print(num)