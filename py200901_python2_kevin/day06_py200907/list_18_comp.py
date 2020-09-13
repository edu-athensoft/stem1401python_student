"""
list comprehension
"""

# case 1.
# [1,2,3,4,5] get a new list by doubling each item

mylist = [1,2,3,4,5]

# solution 1. for-loop
newlist = []
for i in mylist:
    newlist.append(i*2)
print(newlist)


# solution 2. map()
newlist = list(map(lambda item: 2*item, mylist))
print(newlist)


# solution 3. list comprehension
newlist = [x * 2 for x in mylist]
print(newlist)


# case 2. list comprehension and filter
# for, if, []
# [1,3,5,7,9]

newlist2 = [x for x in range(1,11)]
print(newlist2)

newlist2 = [x for x in range(1,11) if x % 2 == 1]
print(newlist2)


