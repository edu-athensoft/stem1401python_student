"""
Homework 4
"""

# 1.
list1 = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
list2 = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']

list3 = dict(zip(list1, list2))
print(list3)

# 2.
names = {'Amy': (22, 92),
         'Lily': (24, 100),
         'Sandy': (21, 87),
         'Peter': (23, 96),
         'Jack': (22, 94)}

names2 = dict(sorted(names.items(), key=lambda x: x[1][0]))
print(names2)

names3 = dict(sorted(names.items(), key=lambda x: x[1][1], reverse=True))
print(names3)

# 3.
candidates = {'Jason': (300, 360, 270),
              'Bill': (280, 340, 291),
              'William': (350, 310, 324)}

allvotes = {}
for i in candidates:
    votes = candidates[i][0] + candidates[i][1] + candidates[i][2]
    allvotes[i] = [votes]

print(sorted(allvotes.items(), key=lambda x: x[1], reverse=True)[0][0])

