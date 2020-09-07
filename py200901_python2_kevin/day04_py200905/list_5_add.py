"""
adding items to a list

append(item)

extend(items)

+ operator
* operator
"""

students = []

# on the 1st day
# students = ['Peter','Amy','Jack']

students.append('Peter')
print(students)

students.append('Amy')
print(students)

students.append('Jack')
print(students)


# on the 2nd day
# 'Tom','Lily','Sarah','Amy'
students.append("Tom")
print(students)
students.append("Lily")
print(students)
students.append("Sarah")
print(students)
students.append("Amy")
print(students)


# on the 3rd day
# 'Tom2','Lily2','Sarah2','Amy2'
students.extend(['Tom2','Lily2','Sarah2','Amy2'])
print(students)


# + operator
# concatenation (combining)
mylist1 = [1,2,3]
mylist2 = [4,5,6]
print(mylist1+mylist2)

print(mylist2+mylist1)
print()

# * operator
print(mylist1 * 1)
print(mylist1 * 2)
print(mylist1 * 3)
print(mylist1 * 0)
print(mylist1 * -1)
print(mylist1 * -5)
