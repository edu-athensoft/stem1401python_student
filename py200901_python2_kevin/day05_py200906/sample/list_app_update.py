"""

application of list

solving problem

"""


# student list of last year
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]
print(stulist)
# you are asked to update the student list for this year
# 101 - 104 is to remove
# 301 - 304 is to change to 311,312,313,314

# update and generate student list of this year
# stulist[:4] = []
# stulist[9:] = [311,312,313,314]
# print(stulist)

# stulist[9:] = [311,312,313,314]
# stulist[:4] = []
# print(stulist)

stulist[:4] = []
print(stulist)

stulist[5:] = [311,312,313,314]
print(stulist)






