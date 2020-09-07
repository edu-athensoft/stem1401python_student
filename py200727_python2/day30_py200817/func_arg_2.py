"""
variable function arguments

default argument
positional argument

case 1. python default argument
"""


#
# def greet(greetings, friend):
#     print(f"{greetings}, {friend}!")
# greet("Good morning", 'Mary')
# greet("Good morning", 'Peter')
# greet("Good morning", 'Jack')


def greet(friend, greetings="Good morning"):
    print(f"{greetings}, {friend}!")


greet('Jack')
greet('Peter')
greet('Mary')

greet('Jack', 'Good afternoon')
print()

# ERROR
# def greet(greetings="Good morning", friend):
#     print(f"{greetings}, {friend}!")

# print('{0} {1} {2}'.format(1,2,3))
# print('{1} {0} {2}'.format(1,2,3))

# ERROR
# def greet(arg1, arg2, arg3="value3", arg4):
#     print()



