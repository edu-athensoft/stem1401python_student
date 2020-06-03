"""
For June 3rd, 2020.
stem1401_python_final_exam_ken
Final Exam.
Kenneth Chen
"""


# Question 1

print("---Question 1: Punctuation remover---")

inputted_string = input("Please input a string: ")
punctuations   =    '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
new_string_as_list = []
new_string = ""

for current_character in inputted_string:
    if current_character not in punctuations:
        new_string_as_list.append(current_character)

print(new_string.join(new_string_as_list))


# Question 2

    # to-do:
    # 1. Save the character the first time it is seen
    # 2. Count the number of times the character appears
    # 3. Print the data in a readable way.

    # Idea:
    # 1. When a new character is spotted, save it inside a dictionary entry as key. Put 1 as value.
        # Like so, each entry will have the word and the number of times it has occured
        # Use for loop to iterate all the characters that have been saved and to check if they have ever appeared.
    # 2. When a character that has already been saved inside the dictionary appears:
        # Add one to the number of times it has occured (value).
        # Like in step one, use for loop to find if character has previously occured.
    # 3. Use a string with 2 placeholders (one for the key (character) and one for the value (times occured).
        # Use a for loop to print out every entry with this template
        # Use items() to make dictionary keys and values into pairs I can assign to variables.

    # Execution:

print("---Question 2: Character frequency counter---")

occurrences_for_every_character = {}
inputted_string = input("Input a string: ")
# backspace for cancelling the effect of the double quotes in the string
template = "The character \"{}\" appeared {} times."
character = None
occurrences = None

for current_character in inputted_string:
    if current_character not in occurrences_for_every_character:
        occurrences_for_every_character[current_character] = 1
    else:
        occurrences_for_every_character[current_character] += 1

for character, occurrences in occurrences_for_every_character.items():
    print(template.format(character, occurrences))


# Question 3

    # to-dos:
        # - find number of characters in set
        # - find number of combinations for a n amount of characters.
        # - print the number of combinations out
        # - make a factorial calculator

    # idea:
        # 1. Use len() to find number of characters
        # 2. Use the mathematical formula to give the number of permutations with no repetition allowed: where n is the number of characters
            # number_of_combinations = n!
        # 3. Use a for loop with range() from 1 to number_of_character+1 and multiply every iteration: factorial

    # execution:

print("---Question 3: Set permutation calculator---")

set1 = {"d","c","a","g","y","e","f","l","3"}
number_of_characters = len(set1)
number_of_permutations = 1

for factorial_calculation in range(1, number_of_characters+1):
    number_of_permutations *= factorial_calculation

print("There are {} permutations for this set of characters.".format(number_of_permutations))