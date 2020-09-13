"""
Ze Yue Li
7/22/2020
1. Read an html document, and find how many <div>, <h1>, <a> tags in the document
2. Save the result as a report file to your file system
[Homework]
"""

file = open("HTML_File")

content = file.read()

div = 0
a = 0
h1 = 0

for i in range(len(content)):
    if content[i] == '<' and content[i+1] == 'd' and content[i+2] == 'i' and content[i+3] == 'v' and content[i+4] == '>':
        div += 1
    elif content[i] == '<' and content[i+1] == 'a' and content[i+2] == '>':
        a += 1
    elif content[i] == '<' and content[i+1] == 'h' and content[i+2] == '1' and content[i+3] == '>':
        h1 += 1

file_2 = open("Result", 'w')

content = "There are " + str(div) + " <div> tags, " + str(a) + " <a> tags, and " + str(h1) + " <h1> tags."

print(content)

file_2.write(content)

file.close()
file_2.close()
