"""
2. Write a Python function that takes two lists and returns True
 if they have at least one common member.
"""

# create two lists
list1 = ['x','2','c']
list2 = ['a','2','3']

#
for item in list1:
    result = item in list2
    if result:
        print(f'the common member is {item}')
        break




