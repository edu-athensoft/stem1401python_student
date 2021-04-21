"""
1. Copy files  (20’)
Description
Copy specific files to the destination.
Your current working directory is set to:   /work/src
Just create it if it does not exist.
Create 3-5 files under /word/src
Then create another directory structure:  /work/dest
Now copy all files under /work/src to /work/dest
Rename all of them by adding a string of current date to the file name before extension.
i.e.   myfile.txt -> myfile_2020-12-20.txt
"""

"""
function:       copy codes missing          10/10
structure:      failed to use function      1.0/2.5
convention:     ok                          2.5/2.5
comment:        missing                     0/2.5
user-friendly:  failed to use exception     1.5/2.5
                title or message missing

subtotal:       15.0
"""


from datetime import date
import os

os.mkdir(r"C:\Users\Li\PycharmProjects\stem1401python\py201220\work")
os.mkdir(r"C:\Users\Li\PycharmProjects\stem1401python\py201220\work\src")
os.mkdir(r"C:\Users\Li\PycharmProjects\stem1401python\py201220\work\dest")

file_num = int(input("How many files would you like to create?"))
for i in range(file_num):
    name = input(f"What will be the name of file No{i+1}?")
    file = open(r"C:\Users\Li\PycharmProjects\stem1401python\py201220\work\src\{}".format(name), "x")
    content = input(f"What will be the content of file No{i+1}?")
    file.write(content)
    file.close()

for i in os.listdir(r"C:\Users\Li\PycharmProjects\stem1401python\py201220\work\src"):
    file_to_write_to = open(f"C:\\Users\\Li\\PycharmProjects\\stem1401python\\py201220\\work\\dest\\{i[:-(len(i) - i.index('.'))]}_{date.today()}{i[-(len(i) - i.index('.')):]}", "x")
    file_to_write_to.write(open(f"C:\\Users\\Li\\PycharmProjects\\stem1401python\\py201220\\work\\src\\{i}").read())
