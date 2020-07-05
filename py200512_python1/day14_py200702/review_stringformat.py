"""
format()
belongs to a string object

template string "", {}
"""


# output a string

print("Hello, {}!".format("Peter"))
print("Hello, {}!".format("Mary"))

name1 = "Peter"
name2 = "Mary"
print("Hello, {}!".format(name1))
print("Hello, {}!".format(name2))

s = "Hello,{}!"
print(s.format(name1))
print(s.format(name2))

# pass multiple values
greeting = "Good morning"
name = "Jackie"
print("{}, {}!".format(greeting, name))

print("{1}, {0}!".format(greeting, name))

print("{greet}, {name}!".format(greet=greeting, name=name))
print("{name}, {greet}!".format(greet=greeting, name=name))


