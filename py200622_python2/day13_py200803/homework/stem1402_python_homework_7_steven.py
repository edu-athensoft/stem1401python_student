"""
stem1402_python_homework_7_steven
"""

print("This program tells you if your string is a pangram or not")
print("A pangram are words or sentence containing every letter of the alphabet")
str1 = input("Please enter a sentence:")
a = 'abcdefghijklmnopqrstuvwxyz'
b = " "


if a:
        if b in str1:
                print(f"'{str1}' is a pangram")
elif a in str1:
    print(f"'{str1}' is a pangram")


else:
        print(f"'{str1}' isn't a pangram")

