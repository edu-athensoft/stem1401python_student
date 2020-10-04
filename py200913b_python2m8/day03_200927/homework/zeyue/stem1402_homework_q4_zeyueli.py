"""
4. Write a Python program to read last n lines of a file.
"""

try:
    f = open("txtfilehomework.txt", "r")
    lines = f.readlines()
    lineNum = int(input("Number of lines to read:"))
    print(lines[len(lines)-lineNum:])
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()