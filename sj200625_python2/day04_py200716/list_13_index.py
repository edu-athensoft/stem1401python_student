"""
index
find all specified items in a list
"""

"""
find the 1st one  with index()
replace
loop:   find next
        till end
output result
"""

mylist = [3, 8, 1, 6, 0, 8, 4, 3, 8, 1, 6, 0, 8, 4]
target_num = 8
tnum = target_num
placeholder = 'x'

result = []

while tnum in mylist:
    # find next with index()
    i = mylist.index(tnum)
    result.append(i)

    # replace
    mylist[i] = placeholder
    print(mylist)

print(result)



