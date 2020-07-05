"""
string format()
"""

username = "Peter"
password = 123
print("Hello",username,'!', "Your password is", password,'.')


# format()
# syntax
# "  {}    ".format(value1, [value2, value3, ...])
# string template

print("Good morning, Marie")
print("Good morning, Peter")
print("Good morning, Jackie")
print("Good morning, Tony")
print()

# {} is the placeholder
print("Good morining, {}")
print("Good morining, {}".format("Marie"))

name = "Peter"
print("Good morining, {}".format(name))
print()

# pass in multiple values
name1 = "Peter"
name2 = "Jackie"
name3 = "Marie"
name4 = "Tony"
greeting1 = 'Good morinig'
greeting2 = 'Good afternoon'
greeting3 = 'Good evening'
greeting4 = 'Good night'
print("{}, {}!".format(greeting1, name1))
print("{}, {}!".format(greeting2, name2))
print("{}, {}!".format(greeting3, name3))
print("{}, {}!".format(greeting4, name4))
print()

# positional arguments
print("{0}, {1}!".format(greeting1, name1))
print("{1}, {0}!".format(greeting1, name1))
print()

#
a = 10
b = 20
c = 30
print("{}, {}, {} ".format(a, b, c))
print("{0},{1},{2}".format(a, b, c))

print("{1},{0},{2}".format(a, b, c))  # just to display in another order, input in a fixed order
print("{0},{1},{2}".format(b, a, c))  # would not recommend

# named or keyword argument
greeting1 = 'Good morinig'
name1 = "Peter"
print("{greet}, {name}!".format(greet=greeting1, name=name1))
print("{name}, {greet}!".format(greet=greeting1, name=name1))


