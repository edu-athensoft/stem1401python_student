"""
print statement and string formatting

for better layout and/or format of text content
"""

x = 5
y = 10

# comment
print(x)
print(y)
print()

print(x,y)
print()

# for users we should output more friendly literals
print("x=",x)
print("y=",y)

print()
print("x=",x,"y=",y)


# str.format()
# string template
# {} is so called placeholder
# format() pass real data/value to replace the placeholders
print("Here x is {}, and y is {}".format(x, y))

print("Here x is", x, ', and y is',y)
