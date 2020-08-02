"""
8. Write a Python function that takes a list of words and
returns the length of the longest one.
"""

"""
wordlist = ['abc','cdef','ab','cdefg','bccc']

longest = wordlist[0]

for word in wordlist:
    # print(word, len(word))
    if len(longest) < len(word):
        longest = word

print("The length of the longest word is {}.".format(len(longest)))
"""

def getlongest(wordlist):
    if len(wordlist) == 0:
        return 0
    else:
        longest = wordlist[0]

        for word in wordlist:
            # print(word, len(word))
            if len(longest) < len(word):
                longest = word

        return len(longest)


# main program
wordlist = ['abc','a','ab']
print(getlongest(wordlist))
