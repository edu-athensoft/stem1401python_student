"""
function variable argument
"""


def foo(x, y):
    print(x, "in function")
    print(y, "in function")

# foo(10,20)

# case 1. foo(10)
# foo(10)

# case 2. foo(10,20,30)
# foo(10,20,30)


def greet(friendname, greetingword="Good morning"):
    print(greetingword, friendname, "!")


greet("Peter","Good morning,")
greet("Jackie","Good morning,")
greet("Mary","Good morning,")
print()

greet("Peter1")
greet("Jackie1")
greet("Mary1")

greet("Mary1", "Good evening")


