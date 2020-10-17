"""
encoding charset
ascii, ASCII,  latin, english alphabet, digit, symbols, punctuations
utf-8

encoding = gbk,  cp1252, utf-8
"""

# case 1.
f = open("file_6.txt")
content = f.read()
print(content)
f.close()


# case 2.
f = open("file_6a.txt", encoding="ascii")
content = f.read()
print(content)
f.close()

