"""
how to access items from a list

by index
starting from 0

index can be counted from left to right

"""

list1 = [345,4654,2,565,789,9,12213]

# access item (element)
res = list1[0]
print(f"The No. 0 item of the list is {res}")

# string.format()
# print("The No. 0 item of the list is {}".format(res))

# to get the item of value of 2
res = list1[2]
print(f"The No. 2 item of the list is {res}")

# get the last item
res = list1[6]
print(f"The No. 6 item of the list is {res}")


# get the length
# length = index of last item + 1
# len()
length = len(list1)
print(f'The length of the list1 is {length}')


# negative index
last_item = list1[-1]
print(f'The last item is {last_item}')


myitem = list1[-5]
print(f'The target item of value 2 is {myitem}')

# access item(s) from a complex(nested) list

