"""
func9. variable arguments

default argument

rule:
positional arguments stay before all the default(keyword) arguments
"""

# def greeting(words="Good morning,", friendname):
#     print(words, friendname, "!")


def greeting(friendname, words="Good morning,"):
    print(words, friendname, "!")


# friendname1 = "Peter"
# greeting(friendname1)
#
# friendname2 = "Mary"
# greeting(friendname2)
#
# friendname3 = "Jackie"
# greeting(friendname3, "Good evening,")





def greeting(friendname="Marie", words="Good morning,"):
    print(words, friendname, "!")

greeting()

friendname2 = "Lily"
greeting(friendname2)

words2 = "Good afternoon,"
greeting(words=words2)

friendname3 = "Jackie"
greeting(friendname3, "Good evening,")

