"""
dictionary method

fromkeys(seq[,v])
"""

# case 1.
dict1 = {}
mydict = dict1.fromkeys(['MON','TUE','WED','THU'])
print(mydict)


# case 2.
dict1 = {}
dict1 = dict1.fromkeys([1,2,3],'UNKNOWN')
print(dict1)

dict1 = dict1.fromkeys([1,2,3],'xyz')
print(dict1)

dict1 = dict1.fromkeys([1,2,3],'abc')
print(dict1)