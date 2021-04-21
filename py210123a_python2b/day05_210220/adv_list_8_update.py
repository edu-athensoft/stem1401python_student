"""
list - update value of items

syntax
list_name[index]=new_value

"""

list1 = ['a','b','c','d','e']
print(list1)

# 'x' -> 'x1'
list1[0]='a1'
list1[1]='b1'
list1[2]='c1'
list1[3]='d1'
list1[4]='e1'

list1[0]='a'

print(list1)


#
odd = [2,4,6,8]

# 2 -> 1
odd[0]=1
print(odd)

# 4,6,8 -> 3,5,7
odd[1] = 3
odd[2] = 5
odd[3] = 7
print(odd)


odd = [1,4,6,8]
#
odd[1:4] = [3,5,7]
print(odd)


#
even = [1, 3, 5, 7, 9]

# 3,5,7 => double 6, 10, 14
even[1:4]= [6,10,14]
print(even)

# for
even = [1, 3, 5, 7, 9]
for item in even:
    print(item)

for i in range(5):
    print(even[i])
    if i>=1 and i<=3:
        # even[i] = 2 * even[i]
        even[i] *= 2

print(even)
print("=======")

even = [1, 3, 5, 7, 9]
#
for i in range(1,4):
    even[i] *= 2
print(even)


# current ultimate solution
even = [1, 3, 5, 7, 9]
newlist = []
for i in range(1,4):
    newlist.append(even[i]*2)
print(even)

even[1:4] = newlist
print(even)


















