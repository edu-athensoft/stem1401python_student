"""
list reverse()
list copy()
"""


my_list = ['p','r','o','b','l','e','m']

my_list.reverse()
print(my_list)


#
target = ['a','b','c']
print('target=',target)
new = target.copy()
print('new=',new)
new.reverse()
print(new)

if new == target:
    print("Yes")
else:
    print("No")




