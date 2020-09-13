"""
22/07/2020
Guang Zhu Cui
[Homework]
1. Read an html document, and find how many <div>, <h1>, <a> tags in the document
2. Save the result as a report file to your file system
"""
print('[info] openning file...')
x = open('HTML_file_to_read.html')
content = x.read()
print(content)
x.close()
print('[done]')
div = '<div>'
b = content.count(div)
a = '<a>'
c = content.count(a)
h1 = '<h1>'
d = content.count(h1)
print('The number of <div> in the html file is {}'.format(b))
print('The number of <a> in the html file is {}'.format(c))
print('The number of <h1> in the html file is {}'.format(d))
