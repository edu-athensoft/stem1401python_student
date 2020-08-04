"""
Check if a list is a pangram

idea: ok


"""

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",\
            "v", "w", "x", "y", "z"]

alphabet_copy = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",\
            "v", "w", "x", "y", "z"]

ispangram = True

user_input = input("")

for i in user_input:
    for j in range(0, len(alphabet)):
        if i == alphabet[j]:
            alphabet[j] = " "

for i in range(0, len(alphabet)):
    if alphabet[i] in alphabet_copy:
        ispangram = False
        break

if ispangram:
    print(f"'{str(user_input)}' is a pangram.")
else:
    print(f"'{str(user_input)}' is not a pangram.")