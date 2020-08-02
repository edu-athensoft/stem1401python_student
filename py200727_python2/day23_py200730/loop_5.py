"""
to get the average of a list of numbers
"""

mylist = [3,4,5,6,7,2,8,9]

# average using while loop

# hint
# mylist[0]     - index of the first item
# mylist[1]
# len(mylist)-1 - index of the last item


# step1. print out (access) all the items


# step2. add them all -> summary


# step 3. get the average= summary / len



sum = 0
avg = sum / len(mylist)

i = 0

size = len(mylist)

while i < size:
    sum = sum + mylist[i]
    i = i + 1

avg = sum / size
print("the average is {}".format(avg))



# qi jun
mylist = [2,3,4,5,6,7,8,9]

sum = 0

average = sum / 8

x = 0

while x < len(mylist):
    sum = sum + mylist[i]
    x = x + 1
average = sum / len(mylist)
print("average:{}".format(average))






