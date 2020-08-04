"""
For August 3rd, 2020.
Ken.
stem1402_python_homeowrk_7_ken

idea: ok

"""

# def pangram_checker(string):
def ispangram(string):

    string = string.lower()

    # global pangram
    pangram = True

    alphabet_checker = {
        "a" : False,
        "b" : False,
        "c" : False,
        "d" : False,
        "e" : False,
        "f" : False,
        "g" : False,
        "h" : False,
        "i" : False,
        "j" : False,
        "k" : False,
        "l" : False,
        "m" : False,
        "n" : False,
        "o" : False,
        "p" : False,
        "q" : False,
        "r" : False,
        "s" : False,
        "t" : False,
        "u" : False,
        "v" : False,
        "w" : False,
        "x" : False,
        "y" : False,
        "z" : False
    }


    for char in string:
        # if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if char in "abcdefghijklmnopqrstuvwxyz":
            alphabet_checker[char] = True

    for valuebool in alphabet_checker:
        # if alphabet_checker[valuebool] == False:
        if not alphabet_checker[valuebool]:
            pangram = False

    return pangram

print("----------- Pangram checker -----------\n")

string = input("Please input the string you would like to check: ")

# pangram_checker(string)

if ispangram(string):
        print("Your string is a pangram.")
else:
        print("Your string isn't a pangram.")