"""
8. Write a Python function that takes a list of
words and returns the length of the longest one.
"""

def getlen(wordlist):
    newlist = []

    for word in wordlist:
        item = (len(word), word)
        newlist.append(item)

    # print(newlist)

    newlist.sort()
    # print(newlist)
    result = newlist[-1][0]
    # print(result)
    return result

wordlist = ['abc', 'ac', 'aabb','bbbccc','dddee']
print(f"The length of the longest one is: {getlen(wordlist)}")



# youran
list1 = ["hellooo", "world", "python"]
result = []


def longest_word(list2):
    for i in list2:
        result.append((len(i), i))


longest_word(list1)
result.sort(reverse=True)
print("The longest words is :", result[0][0])





