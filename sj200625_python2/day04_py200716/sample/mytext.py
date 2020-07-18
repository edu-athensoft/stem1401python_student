"""
my text

goal: to replace all 'my' with 'your'

1. convert the sentence into a list of words
    string.split()

2. iterate over the list
    for-loop
    if the current word == 'my'
        then replace with 'your'

3. combine all words in the list into a string
    ' '.join(iterable)

4. output
    print()

"""

s1 = "this is my demo text this is my demo text this is my demo text " \
     "this is my demo text this is my demo text"

# step 1.
wordlist  = s1.split()
print(wordlist, type(wordlist))

# step 2.
for word in wordlist:
    if word == 'my':
        index = wordlist.index(word)
        wordlist[index] = 'your'
print(wordlist)

# step 3.
result = ' '.join(wordlist)

# step 4.
print(result)

