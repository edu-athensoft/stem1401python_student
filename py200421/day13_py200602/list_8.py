"""
count() 	- Returns the count of number of items passed as an argument
sort()		- Sort items in a list in ascending order
reverse() 	- Reverse the order of items in the list
copy()		- Returns a shallow copy of the list
"""

my_list = ['ring','ring','amulet','amulet','amulet','off-hand','chest armor','chest armor']

# count()
# target = 'amulet'
target = 'ring'

qty_item = 0

for i in my_list:
    if target == i:
        qty_item += 1
print("qty_item=", qty_item, target)


print("qty_item=",my_list.count(target), target)


# sorting
my_list = ['ab','a']
my_list.sort()
print(my_list)

print('ab' > 'a')

my_list = [2,5,1,6,7]
my_list.sort(reverse=True)
print(my_list)


my_list = [2,5,1,6,7]
my_list.reverse()
print(my_list)


# copy()
my_list = [2,5,1,6,7]
x = my_list.copy()
print(x)
print(x is my_list)
print(x == my_list)







