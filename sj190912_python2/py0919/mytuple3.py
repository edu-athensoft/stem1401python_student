# slicing
my_name = "Bill Gates"

# get the first name
# first_name = my_name[0:4]
first_name = my_name[:4]
print(first_name)

# get the last name
# last_name = my_name[5:10]
last_name = my_name[5:]
print(last_name)

print(my_name[:])
print(my_name[0:-1])

# change an element
# my_name[0] = "H"

my_name2 = ['B','i','l','l']
my_name2[0]='H'
print(my_name2)

# conversion
print("conversion")
my_name3 = list(my_name)
print(my_name)
print(my_name3)

my_name4 = tuple(my_name3)
print(my_name4)

