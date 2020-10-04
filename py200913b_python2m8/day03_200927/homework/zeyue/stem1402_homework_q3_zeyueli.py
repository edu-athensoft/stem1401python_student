"""
3. Write a Python program to append text to a file and display the text.
"""

try:
    f = open("txtfilehomework.txt", "a+")
    content = "this is the new text"
    f.write(content)
    print(content)
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)
finally:
    f.close()