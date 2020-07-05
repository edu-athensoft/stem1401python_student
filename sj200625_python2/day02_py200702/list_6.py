"""
add items to a list

extend()
"""

# class2006,  8 students
# 3 new students
# name1, name2, name3, name4, name5, name6, name7, name8
# nm1, nm2, nm3
# print out the list of student name again

namelist = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8']
print("The name list of the old class is {}".format(namelist))

new_students = ['nm1','nm2','nm3']
print("The name list of the new students is {}".format(new_students))

# combine
namelist.extend(new_students)
print(namelist)


# youran
old_students = ["n1", "n2", "n3", "n4", "n5"]
print("Old Students :", old_students)

new_students = ["n6", "n7", "n8"]
print("New Students :", new_students)

New_Class = old_students.extend(new_students)
print(New_Class)


# leon
# Class = namelist.extend(new_students)
# print(Class)

namelist.extend(new_students)
print(namelist)


