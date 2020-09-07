"""
12. Write a Python program to count the occurrences of each word in a given sentence.

problem: performance
option 1.
remove duplicated items before counting

option 2.
remove duplicated items during counting

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
sentence = """
Public health officials reported 11 new cases of COVID-19 in Ottawa as of Saturday afternoon, a return to the double-digit case numbers that have become the norm in recent weeks.

In total, the nation's capital has had 2,698 confirmed cases of the virus since the start of the pandemic.

Around 86 per cent — or 2,316 — of all cases are now considered resolved, with nine of those being resolved since Friday.

There are 37 fewer active cases in the city compared to last Saturday.

The total number of deaths in Ottawa stands at 264, where it has remained since July 28. 

Twelve people remain hospitalized in Ottawa and two people are in intensive care. 

There are also three ongoing outbreaks at city institutions such as long-term care facilities and child-care centres.
"""

# clean
# remove punctuations
sentence = sentence.replace('.','')
sentence = sentence.replace(',','')
sentence = sentence.lower()

print(sentence)

# step 2.
# split()
wordlist = sentence.split()
# wordset = set(wordlist)
# wordset = list(wordset)

print(wordlist)
# print(wordlist)

# step3. count
"""
append() - add one item to a list
"""
result = []
wordset = set()
for word in wordlist:
    if word not in wordset:
        if not word.isnumeric():
            wordset.add(word)
            wordcount = wordlist.count(word)
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







