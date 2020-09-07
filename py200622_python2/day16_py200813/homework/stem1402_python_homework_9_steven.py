"""
stem1402_python_homework_9_steven
"""

# 1. Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty tuples.
# mylist = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


print()
print("-----------------------------------------------------------")


# 2. remove any duplicates from the list

mylist = [1,23,2,4,352,4,352,32]
res1 = []
for i in mylist:
    if i not in res1:
        res1.append(i)

print(f"When we remove duplicates from {mylist} we get {res1}")
print()
print("-----------------------------------------------------------")


# 3. check if list is empty or not

mylist = [1,'sadasd']
if len(mylist) >= 1:
    print(f"{mylist} is not an empty list")
else:
    print(f"{mylist} is an empty list")

print()
print("-----------------------------------------------------------")


# 4. copy or clone a list

mylist = [1,2,3,324,2,'safa','sdgs','gsfhd']
mylist2 = mylist.copy()
print("mylist = ", mylist)
print("mylist2 = ", mylist2)

print()
print("-----------------------------------------------------------")


# 5. find all words longer than 3 from a list

mylist = ['The','quick','brown','fox','jumped','over','the','lazy','dog']
res1 = (f"are the words in {mylist} that are longer than 3")

for i in mylist:
    if len(i) > 3:
        print(f"'{i}'", end=" ")

print(res1)

print()
print("-----------------------------------------------------------")





