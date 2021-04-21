"""
read a file
read(size)
size is counted by byte or char?

here size means the number of char.

"""

file = open("file7.txt", encoding="utf-8")
# file = open("file7.txt", encoding="ascii")

size = 4
content = file.read(size)
print(content)

file.close()