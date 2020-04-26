"""
variable function arguments
default value for arguments
"""


# Function arguments can have default values
# case 2
def greet(name, msg = "Good morning!"):
   print("Hello",name + ', ' + msg)


greet("Kate")
greet("Bruce","How do you do?")
print()


# case 3
def greet2(name="Admin", msg = "Good morning!"):
   print("Hello",name + ', ' + msg)


greet2()
greet2("Kate")
greet2("Bruce","How do you do?")


# case 4
# def greet(msg = "Good morning!", name):
#    print("Hello",name + ', ' + msg)


# greet("Kate")
# greet("Bruce","How do you do?")
# print()
print()

# positional arguments
def greet4(name, groupno, msg = "Good morning!"):
   print("Hello",groupno+':'+name + ', ' + msg)

greet4("Peter","g01")
greet4("Marie","g01","How do you do?")


# def greet4(name, msg = "Good morning!", groupno):
#     pass



# define your function with two parameters
# call it with two arguments
# one argument must be a default-argument
