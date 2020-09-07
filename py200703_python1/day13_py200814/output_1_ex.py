"""
string.format()

friend1 = 'Marie'
friend2 = 'Peter'
friend3 = 'Jack'
friend4 = 'Amy'

write a program to greet to every one
Output:
Good afternoon, XXXX !

"""


# lucas
friend1 = 'Marie'
friend2 = 'Peter'
friend3 = 'Jack'
friend4 = 'Amy'
print("Good afternoon,",friend1,",",friend2,",",friend3,"and",friend4,"!")

print("Good morning, {}".format(friend1))
print("Good morning, {}".format(friend2))
print("Good morning, {}".format(friend3))
print("Good morning, {}".format(friend4))
print("\n")

#
# option = 'morning'
option = 'afternoon'
# option = 'evening'
# option = 'night'

# flexible with a pattern
print("Good {}, {}!".format(option, friend1))
print("Good {}, {}!".format(option, friend2))
print("Good {}, {}!".format(option, friend3))
print("Good {}, {}!".format(option, friend4))
print("\n")

# special cases
print("Good {}, {}!".format(option, friend1, 'extra'))
print("Good {}, {}!".format(option))


mylist = [1,2,3,4,5,6]
mytuple = (1,2,3,4,5,6)







