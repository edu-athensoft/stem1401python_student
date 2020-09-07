"""
12. Write a Python program to count the occurrences of each word in a given sentence.

problem: performance
option 1.
remove duplicated items before counting



"""

"""
plan
1. write sentence
2. split sentence and get the list of word
3. count each word
    iterate
4. output
"""

# step 1. write sentence
sentence = "aa bb cc aa bb cc dd ee cc ee dd ff"
print(sentence)

# step 2.
# split()
wordlist = sentence.split()
wordset = set(wordlist)
wordset = list(wordset)

print(wordlist)
# print(wordlist)

# step3. count
"""
append() - add one item to a list
"""
result = []
for word in wordset:
    wordcount = wordlist.count(word)
    # print(f"{word}:{wordcount}")
    # entry = (word, wordcount)
    entry = word, wordcount
    print(entry, type(entry))
    result.append(entry)
# print(result)

# step4. output
# remove duplicated items
# use a dictionary
"""
option 1.
create a dict, then put each item into the dictionary

option 2.
convert to dict
dict()
"""
result.sort()
print(dict(result))







