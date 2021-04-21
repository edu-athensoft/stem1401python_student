"""
solution 1.
1. len(s) >=2
2. the first char of string 's'    s[0]
   the last char of string 's'     s[-1]
"""

stringlist = ['1221','2323','asdf','adda','asdfasdf','1111','ab','aa','c']

# create a list for result
results = []

# check every item in the list
for item in stringlist:
    print(item)

    # check if the string is ok, then put it into the result list
    if len(item)>=2 and item[0] == item[-1]:
        results.append(item)

# test
print(results)
print(len(results))


mystr = input('enter a string:')
print(mystr)