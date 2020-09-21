"""
Using dictionary to count every char in a given string
"python is a good language"
Expected result:
p: 1
y: 1
t: 1
h: 1
o: 3
...
"""

"""
idea:
1. determine using data type of dictionary
key : value
char : count

2. initial
char : 0

3. core logic
if key not exist (occurs for the 1st time), adding
else update by increasing 1 to the value
iteration is needed.
for-loop
"""


str1 = "python is a good language"

charcount = {}

for char in str1:
    print(char)
    if char not in charcount:
        charcount[char] = 1
    else:
        charcount[char] += 1

print(charcount)

