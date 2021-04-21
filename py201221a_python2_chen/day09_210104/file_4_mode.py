"""
file mode

Read and Write Mode

Mode        Description
r           open a file for reading (default)

w           open a file for writing (not default)
x           open a file for exclusive creation
a           open a file for appending content at the end of the file.


Text and Binary Mode
t           text (default)
b           binary

rb is default mode (complete form)

Additional Mode
+           open a file for updating (reading and writing)


"""


f = open('test.txt')
f = open('text.txt', 'w')
f = open('test.jpg','rb')
f = open('test.txt', encoding='utf-8')
