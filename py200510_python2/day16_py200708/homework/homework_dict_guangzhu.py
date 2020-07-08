mydict = {'a':1, 'b':2, 'c':3, 'd':0.5}
list1 = []
for i in list(mydict):
    list1.append(mydict[i])
list1.sort(reverse = True)
dict1 = {'1': list1[0],
         '2': list1[1],
         '3': list1[2],
         '4': list1[3]}
print(dict1)