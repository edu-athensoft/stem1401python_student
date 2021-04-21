"""
file read()

read(size)
read by size of char

cursor

absolute path    \  in windowns
relative path    /
"""


# file = open("homework/csvdata.csv")
file = open("file_1.txt", encoding="utf-8")

# size - integer
# size - char or byte
# size - number of char
content = file.read(6)
print(content)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf4 in position 207: invalid continuation byte

content = file.read(6)
print(content)

content = file.read(6)
print(content)

file.close()



