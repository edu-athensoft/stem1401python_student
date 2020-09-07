"""
find all specified items from a list
"""

# my_list = ['p','r','o','b','l','e','m','p','r','o','b','l','e','m','p','r','o','b','l','e','m']
my_list = ['p','r','o','b','l','e','m'] * 3

# find letter of 'o'

# solution 1.
myindex = []
next_index = -1
for item in my_list:
    if item == 'o':
        next_index = my_list.index(item, next_index+1)
        print(next_index)
        myindex.append(next_index)
print(myindex)
print()


# solution 2.
myindex = []
for index in range(len(my_list)):
    if my_list[index] == 'o':
        # print(index)
        myindex.append(index)

print(myindex)
print()


# solution 3. based on solution 2
def getIndexOf(target):
    myindex = []
    for index in range(len(my_list)):
        if my_list[index] == target:
            myindex.append(index)
    return myindex

target_index = getIndexOf('r')
print(target_index)
print()

# solution 4. based on solution 1
def getIndexOf2(target):
    myindex = []
    next_index = -1
    for item in my_list:
        if item == target:
            next_index = my_list.index(item, next_index + 1)
            print(next_index)
            myindex.append(next_index)
    # print(myindex)
    return myindex

target_index = getIndexOf2('o')
print(target_index)


# replace all
# find all -> replace all
# using function
