"""
sort() - sort items in a list in ascending order

descending order
"""

mylist = ['It','is','my','favorite','music','isn\'t','it']
a = mylist.sort()
print(a, type(a))
print(mylist)
print()

mylist = ['It','is','my','favorite','music','isn\'t','it','',' ','\t','\n']
a = mylist.sort()
print(mylist)

mylist = ['It','is','my','favorite','music','isn\'t','it','',' ','\t','\n']
a = mylist.sort(reverse=True)
print(mylist)