"""
String
a sequence of characters
iterating through a string
"""

str1 = 'hello world'

for char in str1:
    print(char)



# ex. please count how many chars of 'o' in the string
# basic idea
# iterating through the string and count (by comparing)

counter = 0

for i in str1:
    if i == "o":
        # print(len(i))
        counter += 1

print(f'There are {counter} of char o in the \'{str1}\'')


# print out every index of 'o'
# basic idea
# index
# str1[0], str1[1], str1[2], ...


for i in range(len(str1)):
    if str1[i] == 'o':
        print(i, str1[i])



# basic idea
counter = 0  # the same as index of beginning

for c in str1:
    # counter += 1
    if c == "o":
        print(c, 'at index of',counter)
    counter += 1
