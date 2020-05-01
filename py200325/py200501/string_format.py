"""
output
print
string format()
"""

print("This is my book.")

print("This is my bike.")

print("This is my pen.")

# pattern
# string pattern

# "This is my {}"

# {} is the placeholder
# string template

print("This is my {}")
# pass a literal
print("This is my {}".format("pen"))

# pass a variable
thing = "pen"
print("This is my {}".format(thing))

# pass a variable
template = "This is my {}"
thing = "pen"
print(template.format(thing))


# pass mutliple values
thing1 = "pen"
thing2 = "bike"
print("This is my {} and {}".format(thing1, thing2))


# pass
print("This is my {} and {}".format(thing2, thing1))

# to specify the order
# arguments of the function - format()
# positional argument
print("This is my {0} and {1}".format(thing1, thing2))
print("This is my {1} and {0}".format(thing1, thing2))


thing1 = "pen"
thing2 = "bike"
thing3 = "desk"
thing4 = "ipad"
print("This is her {1} and {0}; and her {3} is on the {2}.".format(thing1, thing2, thing3, thing4))

# named argument
print("This is her {t2} and {t1}; and her {t4} is on the {t3}.".format(t1=thing1, t2=thing2, t3=thing3, t4=thing4))

# compare print(),  print string.format()



