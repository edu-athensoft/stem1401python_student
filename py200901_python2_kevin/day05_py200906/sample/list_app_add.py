"""

using append(), extend()
+

basic idea:
1. split the original list into 3 sub-lists
2. append or extend additional students at the tail of each sub-list
3. combine them in ascending order
"""


# student list of last year
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]

# year
# students 105 transferred from another school to this school
# students 206,207 transferred from another school to this school
# students 305,306,307 transferred from another school to this school
# students 304 transferred to another school

# please re-generate the student list

"""
step 1. split the original list into 3 sub-lists
"""
# pick up all students from class #1
stuclass1 = stulist[:4]
print("students in class #1 is {}".format(stuclass1))

# pick up all students from class #2
stuclass2 = stulist[4:9]
print("students in class #2 is {}".format(stuclass2))

# pick up all students from class #3
stuclass3 = stulist[9:]
print("students in class #3 is {}".format(stuclass3))
print()


"""
step 2. append or extend additional students at the tail of each sub-list
"""
# processing class #1
stuclass1.append(105)
print("stuclass1",stuclass1)

# processing class #2
stuclass2.extend([206,207])
print("stuclass2",stuclass2)

# processing class #3
stuclass3.extend([305,306,307])
print("stuclass3",stuclass3)

# stuclass3[3] = []
stuclass3[3:4] =[]
print("stuclass3",stuclass3)
print()

"""
step 3. combine them in ascending order
"""
new_studentlist = stuclass1 + stuclass2 + stuclass3
print("The new student list is {}".format(new_studentlist))




