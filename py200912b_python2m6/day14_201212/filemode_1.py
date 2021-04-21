"""
file mode

r
w
a
x

t,b

+

write a program to have a trial with r+

"""


# kevin

f1 = open("filemode_1.txt", 'x')
f1.close()


file = open("filemode_1.txt", 'r+')
content = file.read()
print(content)

comment = "asdfjamdsndfnsajkf"
file.write(comment)

content = file.read()
print(content)

file.close()
print("The first comment is has been write")


"""
file = open("filemode_1.txt", 'r+')
file.read()
comment = "asdfjamdsndfnsajkf22222222222"
file.write(comment)
file.close()
print("The second comment is has been write")

"""

