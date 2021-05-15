"""
sample code
"""

# check if a list is empty
def isempty(mylist):
    if mylist:
        print(f'The list is {mylist}')
    else:
        print('The list is empty.')


def isempty2(mylist):
    if len(mylist)!=0:
        print(f'The list is {mylist}')
    else:
        print('The list is empty.')


# main program
print("case 1. ====")
mylist = [1,2,3]
isempty(mylist)
isempty2(mylist)

print("case 2. ====")
mylist = []
isempty(mylist)
isempty2(mylist)


