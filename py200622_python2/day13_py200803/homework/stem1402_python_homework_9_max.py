"""
Homework 9.  max

idea: ok


"""

def pangram_check(mystr):

    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    # alpha = 'abcdefghijklmnopqrstuvwxyz'

    # times of execution
    for x in mystr:
        for y in alpha:

            if x == y:
                alpha.remove(y)

    if len(alpha) < 1:
        print("This is a pangram")
    else:
        print("This is not a pangram")

# input from kbd
mystr = input("Please input a sentence: ")

pangram_check(mystr)