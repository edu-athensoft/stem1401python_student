"""
# year 2019
# students 105 transferred from another school to this school
# students 206,207 transferred from another school to this school
# students 305,306,307 transferred from another school to this school
# students 304 transferred to another school

# year 2020
# you are asked to update the student list for this year
# 101 - 104 is to remove
# 301 - 304 is to change to 311,312,313,314


solution 1
basic idea:
1. split the original list into 3 sub-lists
2. append or extend additional students at the tail of each sub-list
3. combine them in ascending order
"""

# student list of last year
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]

# please re-generate the student list