"""
final_exam_steven
"""
# 1.

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

sentence = input("Please enter a string:")
final_sentence = ""

for i in sentence:
    if i not in punctuations:
        final_sentence += i

print("You sentence without punctuations is: {}".format(final_sentence))
print("------------------------------------------------")


# 2.

dict1 = {}

for i in final_sentence:
    if i not in dict1:       # if the character isn't in dict1
        dict1[i] = 1         # the count of that character becomes 1
    else:
        dict1[i] += 1        # if the character is already in dict1
                             # the count of that character increases by 1
print("The count of all the characters in {} is: {}".format(final_sentence, dict1))




































