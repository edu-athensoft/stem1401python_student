"""

application of list

solving problem

solution 1. starting with digit x


"""

# list of student in 3 classes
# the items must be in order , ascending or descending
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]

# task 1
# pick up all students from class #1
stuclass1 = stulist[:4]
print("students in class #1 is {}".format(stuclass1))

# task 2
# pick up all students from class #2
stuclass2 = stulist[4:9]
print("students in class #2 is {}".format(stuclass2))

# task 3
# pick up all students from class #3
stuclass3 = stulist[9:]
print("students in class #3 is {}".format(stuclass3))

