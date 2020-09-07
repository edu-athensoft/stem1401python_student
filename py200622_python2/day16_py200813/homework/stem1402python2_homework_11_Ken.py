"""
For August 13th, 2020.
stem1402python2_homework_11_Ken
Ken
"""

# Question 1

def secondelement(el):
    return el[1]

list1 = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

list1.sort(key=secondelement)

print(list1)


# Question 2

list2 = [1,3,2,4,2,1,2,3,1]
listdup = []

def remduplicates(list):
    for char in list:
        if char not in listdup:
            listdup.append(char)
    return listdup

print(remduplicates(list2))


# Question 3

def listemptyinstance(list):
    if list == []:
        return True
    else: return False

print(listemptyinstance([]))



# Question 4
list4 = [1,2,3]

def copylist(list):
    list = []
    for char in list:
        list.append(char)

list44 = copylist(list4)

print(list44 is list4)


# Question 5

string5 = "The quick brown fox jumps over the lazy dog"

def wordseparator(string):
    list = [string]
    return list[0].split()

def findmorethan3char(string):
    list = []
    for words in wordseparator(string):
        if len(words) > 3:
            list.append(words)
    return list

print(findmorethan3char(string5))