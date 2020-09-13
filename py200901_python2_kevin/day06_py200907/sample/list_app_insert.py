"""

using insert()

basic idea:
1. insert students
2. remove student 304
"""


# student list of last year
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]

# year
# students 105 transferred from another school to this school
# students 206,207 transferred from another school to this school
# students 305,306,307 transferred from another school to this school
# students 304 transferred to another school

# please re-generate the student list
stu_list = [101, 102, 103, 104, 201, 202, 203, 204, 205, 301, 302, 303, 304]
stu_list.insert(4, 105)
stu_list[10:10] = [206, 207]
stu_list[15:15] = [306, 307]
stu_list.remove(304)
print(stu_list)


# chengjun
stulist = [101, 102, 103, 104, 201, 202, 203, 204, 205, 301, 302, 303, 304]
stulist.insert(4, 105)
stulist[10:10] = [206, 207]
stulist[15:15] = [306, 307]
stulist.remove(304)
print(stulist)










