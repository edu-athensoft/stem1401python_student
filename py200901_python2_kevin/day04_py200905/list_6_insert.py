"""
insert items to a list
"""

odd = [1, 9]

# case 1. insert one item
odd.insert(1,3)
print(odd)

# case 2. insert multiple items
odd[2:2] = [5,7]
print(odd)


# ex.
students = ['Peter', 'Amy', 'Jack']
# please insert 'Sarah','Tom' right after 'Peter' and before 'Amy'
students[1:1] = ["Sarah","Tom"]
print(students)


