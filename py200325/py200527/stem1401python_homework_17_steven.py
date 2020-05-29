"""
Quiz 9
"""

# Question 1

# if
if 5 == 6:
    print("ok")

# if - else
if 5 == 7:
    print("okay")
else:
    print("not okay")

# if - else - elif
if 5 == 7:
    print("bad")
elif 6 == 6:
    print("good")
else:
    print("maybe")

# nested if
if 5 == 5:
    if 5 == 6:
        print("ok")
    else:
        print("no")
else:
    print("yes")


# Question 2

list1 = [2,325,234,253,3,5,5,454,31,432]

biggest = list1[0]
smallest = list1[0]

for number in list1:
    if biggest < number:
        biggest = number
    if smallest > number:
        smallest = number

print("{} is the biggest number, and {} is the smallest number.".format(biggest, smallest))


# Extra question

product = 1
for i in range(1,101):
    product = product * i

print("Product of 1 to 100 is {}".format(product))












