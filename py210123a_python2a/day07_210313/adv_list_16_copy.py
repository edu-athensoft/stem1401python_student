"""
copy()
returns a shallow copy of the list

"""

odd = [1,2,10,31,5,10,7,9,10,12,14,10]

newodd = odd
# 1 -> 100
odd[0] = 100
print(newodd)



odd = [1,2,10,31,5,10,7,9,10,12,14,10]
odd2 = odd.copy()
odd[0] = 100
print(odd)
print(odd2)













