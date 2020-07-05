"""
Quiz 10
"""

# Question 2
product = 1

for i in range(2,20,2):
    product = product * i

print("Product 1 x 2 x 4 x 6 ... x 20 is {}".format(product))


# Question 3
Marie = 85
Phoebe = 78
Sabrina = 96
Emma = 85
Amy = 73
Isabelle = 59
Clark = 45

all = [Marie, Phoebe, Sabrina, Emma, Amy, Isabelle, Clark ]

average = ((Marie + Phoebe + Sabrina + Emma + Amy + Isabelle + Clark) / len(all))
print("The average of all the students is {:.0f}.".format(average))

# I didn't really do the last part










