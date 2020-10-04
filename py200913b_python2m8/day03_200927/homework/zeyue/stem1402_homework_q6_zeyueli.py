"""
6. Write a Python program to read a file line by line store it into a variable.
"""

try:
    f = open("txtfilehomework.txt", "r")
    lines = f.readlines()
    linesVar = ""
    for i in lines:
        linesVar += i
    print(linesVar)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()