"""
built-in function
sorted()
"""


mydict = {3:'a', 6:'f', 1:'c'}

result = sorted(mydict)
print(result, type(result))


# question
# how to sort a dictionary by key?

sortedkeys = sorted(mydict)

str1 = ''
for key in sortedkeys:
    # print(key, mydict[key])
    str1 += "{}:{}, ".format(key, mydict[key])

print('{',str1[:-2],'}')


