"""
using arbitrary argument technique

input 3 arguments of the names

to print out greeting words to 3 people
How do you do, Peter?
How do you do, Marie?
How do you do, Sarah?

Do not use loop
"""

def foo(*thing):
    for i in thing:
        print("How are you {} ?".format(i))
        # print("How are you {} ?".format(i))
        # print("How are you {} ?".format(i))

# thing = ("Peter", "Arthur", "Anthony")

foo("Peter", "Arthur", "Anthony")