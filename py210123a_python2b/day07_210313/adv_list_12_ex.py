"""
remove specified items by value
"""

odd = [1,2,10,3,5,10,7,9,10,12,14,10]

"""
idea:
if value exists:
    remove(value)
else:
    do nothing
    
terminate when value does not exists 
"""

"""
value = 10
# odd.remove(99)

if value in odd:
    odd.remove(value)

if value in odd:
    odd.remove(value)

print(odd)
"""

value = 10

while value in odd:
    odd.remove(value)

print(odd)


