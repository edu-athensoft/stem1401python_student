"""
dictionary method

fromkeys()
"""


keys = ("k1", "k2", "k3")

# case 1. generate a dictionary without providing default value
mydict = {}
mydict = mydict.fromkeys(keys)
print(mydict)


# case 2. generate a dictionary providing default value
mydict = {}
mydict = mydict.fromkeys(keys,0)
print(mydict)

# counting the letters in a given string
# "asdfjasdjfasjdfasjdfkasdjfklasjkdfl;as;dfksdf  asdfas f  asd f asdf "
# a = 10
# s = 8
# ; = 4
