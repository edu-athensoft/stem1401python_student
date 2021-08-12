"""
for-loop

syntax
for item in sequence:
   body of for-loop

access
    read or write

determined length/times

"""

# print out a paragraph for 3 times

# counter
mylist = [0,0,0]

for item in mylist:
    print("sentence 1.")
    print("sentence 2.")
    print("sentence 3.")
    print()

print("============")
mylist = [0,0,0,0,0,0,0,0,0]
print(len(mylist))

for item in mylist:
    print("sentence 1.")
    print("sentence 2.")
    print("sentence 3.")
    print()

print("===end===")