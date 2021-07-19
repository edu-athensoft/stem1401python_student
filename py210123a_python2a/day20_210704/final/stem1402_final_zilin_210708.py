"""
1.
No, the comparison between floating number are not always accurate because
the addition between two floating number doesn't have the exact answer so there
can have errors in the comparison. For example: 1,2 + 1.7 != 2.9

2.
from decimal import Decimal as D

print(D(1.1))

3.
from decimal import Decimal as D

print(D(1/3))
print(D(2/3))

print(D(1/3 + 2/3))

4.
A string is a sequence of characters, it is immutable.

5.
str = "890abc123"
substr = str[3:6]
print(substr)

6.
import random

res = random.randint(1, 6)
print(res)

7.
import random

for i in range(100):
    res2 = random.randint(0,1)
    print(res2)

8.
import random

str1 = '1,2,3,4,5,6'

for i in str1:
    a = random.choice(str1)

print(a)

9.
We use list and tuple when we want to have multiple items in one list or one tuple.

10.
We use set and dictionary when we want to crate an unordered collection of items.
"""

# 1

import random

list1 = []

for i in range(100):
     res = random.randint(0,1000)
     list1.append(res)

print(list1)

# the biggest number
print(max(list1))
# the smallest number
print(min(list1))

print()
print("============")
print()

# 2

string1 = 'aabbccdd112233'

set1 = set(string1)
print(set1)

result = ''.join(set1)
print(result)

result2 = sorted(result)
print(result2)

result3 = ''.join(result2)
print(result3)

print()
print("===========")
print()

# 3

cipher_text = "84 104 105 115 32 105 115 32 97 32 112 121 116 104 111 110 32 115 111 117 114 99 101 32 99 111 100 101 46 "
list1 = list(cipher_text.split())
print(list1)

new_list = []

for i in list1:
    if i == '84':
        new_list.append("T")
    if i == '104':
        new_list.append("h")
    if i == '105':
        new_list.append("i")
    if i == '115':
        new_list.append("s")
    if i == '32':
        new_list.append(" ")
    if i == '97':
        new_list.append("a")
    if i == '112':
        new_list.append("p")
    if i == '121':
        new_list.append("y")
    if i == '116':
        new_list.append("t")
    if i == '111':
        new_list.append("o")
    if i == '110':
        new_list.append("n")
    if i == '117':
        new_list.append("u")
    if i == '114':
        new_list.append("r")
    if i == '99':
        new_list.append("c")
    if i == '101':
        new_list.append("e")
    if i == '100':
        new_list.append("d")
    if i == '46':
        new_list.append(".")


print(new_list)

res = ''.join(new_list)
print(res)







