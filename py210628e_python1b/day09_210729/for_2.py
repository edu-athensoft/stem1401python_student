"""
for-loop
"""

mylist = [11,22,33,44,55,66,77,88,99]

# printing each item

print("===start===")

for x in mylist:
    print("The current item is {}".format(x))
    result = x + 1
    print("The current item is {}".format(result))
    print("The current item is {}".format(str(x)+"th time"))
    print()


# for item in mylist:
#     print("The current item is {}".format(item))
#     print("The current item is {}".format(item))
#     print("The current item is {}".format(item))

print("===end===")

