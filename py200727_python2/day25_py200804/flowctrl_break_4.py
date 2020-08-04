"""
project:

user can input a word
if the word contains the letter of i
please do not show the letter of i,
otherwise show every letter of that word

i.e.:  >>  apple
output: apple

i.e.:  >> string
output: str
and exit

"""

word = input("Enter a word:")
# print(word)

for char in word:
    # print(char, end=',')
    if char == 'i':
        break
    print(char, end="")


# kevin
word = list(input("Please input a word: "))

for letter in range(len(word)):
    if "i" in word[letter]:
        break
    print(word[letter],end="")





