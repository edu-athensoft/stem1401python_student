"""
Homework

Date: 2021-03-21
Create a tuple with 8 items
A story or topic must be applied as you did with list in class
calculate and print out the number of items

Question:
if you try to write code to modify values of item, what message may occur?
please write code and run it and then copy that error message into your document.
Due date: by the end of next Sat.

write your docstring here
"""

drinks = ('coca cola', '7up', 'Sprite', 'soda water', 'Red Bull', 'Monster Energy')
# drinks = ['coca cola', '7up', 'Sprite', 'soda water', 'Red Bull', 'Monster Energy']
print(drinks)

print(type(drinks))  ###

num = len(drinks)
print("There are", num, "items in the list")


# TypeError: 'tuple' object does not support item assignment
# drinks[0] = 'Spring Water'


"""

q1:
answer: ?

"""