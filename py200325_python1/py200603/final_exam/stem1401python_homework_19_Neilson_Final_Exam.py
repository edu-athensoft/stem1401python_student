"""
Final Exam
"""

# Question 1 remove all special characters in a inputed string
# "!()-[]{};:\,<>./?@#$%^&*_~"
special_characters = ["\"", "(", ")", "-", "[", "]", "{", "}", ";", ":", "\\", "<", ">", ".", "/", "?", "@", "#", "$", "%", "^", "&", "*", "_", "~"]

string = list(input("Please input whatever you want and then the program will remove all special characters: "))
final_string = ""
for i in string:
    if i not in special_characters:
        final_string += i
    else:
        pass
print("This is your string without special characters:\n{}".format(final_string))


# Question 2 find the number of times a letter occurred in a word or sentence
count = 0
phrase_or_word = list(input("Please input a sentence or word: "))
different_characters = []
for i in phrase_or_word:
    if i not in different_characters:
        different_characters.append(i)
    else:
        pass
different_characters.sort()
for j in different_characters:
    for i in phrase_or_word:
        if i == j:
            count += 1
        else:
            pass
    print("The number of the character {} is {}.".format(j, count))
    count = 0

# Question 3 list the number of all different combinations of numbers(different)
numbers = [3, 5, 7, 2, 4]
num_of_ways = 1

for i in range(1, len(numbers) + 1):
    num_of_ways *= i
print()
print("The given numbers are {}.".format(numbers))
print("The number of combination we can make with these numbers is {}".format(num_of_ways))


