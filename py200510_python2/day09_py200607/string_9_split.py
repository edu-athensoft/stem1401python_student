"""
string method - split()
"""

# case 1
my_str= "This will split all words into a list"
print(my_str)

a = my_str.split()
print(a, type(a))
print()


# case 2
my_str= "This  will   split all.words into a list"
print(my_str)

a = my_str.split()
print(a, type(a))
print()


# case 3
my_str= "This,  will,   split, all words, into, a list"
print(my_str)

a = my_str.split(',')
print(a, type(a))
print()