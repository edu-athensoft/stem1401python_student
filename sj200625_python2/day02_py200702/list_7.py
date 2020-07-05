"""
generate list
combing or repeating
"""

# + operator
list1 = [1,2,3]
list2 = [4,5,6]
newlist = list1 + list2
print(newlist)

newlist = list2 + list1
print(newlist)


#
old_students = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8']
new_students = ['nm1','nm2','nm3']
namelist = old_students + new_students
print(namelist)


#
old_students = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6', 'name7', 'name8']
new_students = ['nm1','nm2','nm3']

for new in new_students:
    old_students.append(new)
print(old_students)


# repeating a list
# * operator
list1 = [1,2,3]
newlist = list1 * 3
print(newlist)

newlist = list1 * 0
print(newlist)

newlist = list1 * -1
print(newlist)




