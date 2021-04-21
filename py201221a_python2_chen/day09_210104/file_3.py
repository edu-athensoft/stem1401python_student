"""
to open a file at different location (path)

returns a file object
"""


try:
    file = open("testdir/text2.txt")
    print(file)

except FileNotFoundError as fe:
    print(fe)