"""
break in for loop

if index ==6 ,then exit
"""


mylist = [1,2,3,4,5,6,67,8,9,0]


for i in range(len(mylist)):

    print("hello")

    if i == 6:
        break

    print(mylist[i])

print("end")
