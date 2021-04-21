"""
1. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
"""

import string

result = [open(f"{letter}.txt", "w") for letter in string.ascii_uppercase]

print(result, type(result))
