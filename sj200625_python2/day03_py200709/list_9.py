"""
remove item(s) from a list

remove() - remove by value
pop() - remove by index

"""

stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304,401,401]

stulist.remove(304)
print(stulist)

stulist.remove(205)
print(stulist)

# remove an item which does not exist in the list
if 205 in stulist:
    stulist.remove(205)
    print(stulist)

# remove all 401
stulist.remove(401)
print(stulist)

stulist.remove(401)
print(stulist)


print("\npop()")
# pop() - remove the last item
stulist = [101,102,103,104,201,202,203,204,205,301,302,303,304]
stulist.pop()
print(stulist)

stulist.pop()
print(stulist)

stulist.pop()
print(stulist)

# pop(index)
# index of 102 = 1
stulist.pop(1)
print(stulist)

stulist.pop(-1)
print(stulist)

# clear() - remove all
print("\nclear()")
stulist.clear()
print(stulist)

# delete items
my_list = ['p','r','o','b','l','e','m']
# remove 'o'
my_list[2:3] = []
print(my_list)

my_list[2:5]=[]
print(my_list)


