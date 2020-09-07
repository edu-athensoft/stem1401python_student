"""
list method
index()
"""

# student list of last year
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]

# get the position of student 201 in the list
stu_no = 201
print("The student {} is at stulist[{}]".format(stu_no,stulist.index(stu_no)))

# get the position of student 201 in the list
stu_no = 301
print("The student {} is at stulist[{}]".format(stu_no,stulist.index(stu_no)))


stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304,101,102,103,104,201,202,203,204,205,301,302,303,304]
# get the index of 2nd item of 201
stu_no = 201
current_index = stulist.index(stu_no)
print("The 1st student {} is at stulist[{}]".format(stu_no,current_index))
print("The 2nd student {} is at stulist[{}]".format(stu_no,stulist.index(stu_no,current_index+1)))