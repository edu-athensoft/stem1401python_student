"""
please convert a for loop to a while loop

1+2+3+4+....+10 = 55

1+2+3+ +5....+10 = 51
(no 4)

"""

# step1. write a for-loop



# step2. convert the for-loop to a while-loop
# hints:
# set a counter
# find the upper limit or lower limit which
# can make loop terminate
# pay attention to the boundary

sum = 0
i = 1

while i <= 10:
    sum = sum + i
    i += 1

print("The answer is {}.".format(sum))


# qi chen
x = 0
y = 1

while y <= 10:
    x = x + y
    y += 1

print("answer:{}".format(x))
print()




