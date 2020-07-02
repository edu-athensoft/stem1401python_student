"""
variable arguments
"""


def foo1(x,y):
    print(x)
    print(y)


# TypeError: foo1() missing 1 required positional argument: 'y'
# foo1(1)

# TypeError: foo1() takes 2 positional arguments but 3 were given
# foo1(1,2,3)




def greeting(friendname, words):
    print(words, friendname, "!")


friendname1 = "Peter"
greeting(friendname1, "Good morning,")

friendname2 = "Mary"
greeting(friendname2, "Good morning,")

friendname3 = "Jackie"
greeting(friendname3, "Good morning,")