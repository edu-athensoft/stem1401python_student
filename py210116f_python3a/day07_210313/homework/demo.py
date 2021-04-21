"""
extract url from a string

"""

mystr = "Here's a link of a picture of a samoyed: http://sonderlives.com/wp-content/uploads/2018/08/samoyed11.jpg"

# step1. find 'http'
TARGET = 'http'
if TARGET in mystr:
    pos = mystr.index(TARGET)
    print(pos)
else:
    pos = -1

url = mystr[pos:]
print(url)