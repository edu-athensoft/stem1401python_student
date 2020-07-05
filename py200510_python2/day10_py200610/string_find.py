"""
string - find substring
string.find()
return the index of the initial char
return -1 if it cannot be found
"""

my_str = "Happy new year"

# find 'ew'
pos = my_str.find('ew')
print("The first substring of 'ew' is at {}".format(pos))

# cannot find out, return -1
pos = my_str.find('x')
print("The first substring of 'x' is at {}".format(pos))

# find from start pos
print(my_str.find('ea',9))

# find from start pos to stop pos
my_str = 'Happy New Year ew aaa bbb cewcc'
print(my_str.find('ew',17, 30))
print()


# find from right to left
# rfind()
print(my_str.rfind("ew"))


# find all





