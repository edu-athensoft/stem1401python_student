"""
Quiz 9
"""

# 1.

# var 1 - if
ddd = 1

if ddd == 1:
    print("ddd = 1")

# var 2 - if, else
ddd = 1

if ddd == 2:
    print("ddd = 1")
else:
    print("ddd \u2260 1")

# var 3 - if, elif, else
ddd = 2

if ddd == 1:
    print("ddd = 1")
elif ddd == 2:
    print("ddd = 2")
else:
    print("ddd \u2260 1 or 2")

# var 4 - nested if
ddd = 3

if ddd > 1:
    if ddd > 2:
        if ddd > 3:
            print("ddd is larger than 3")
        else:
            print("ddd is larger than 2")
    else:
        print("ddd is larger than 1")
else:
    print("ddd is smaller than 1")

# 2.

list1 = [20, 22, 86, 75, 24, 92, 54, 21, 69, 81]

num1 = list1[0]
num2 = list1[0]
for i in list1:
    if num1 < i:
        num1 = i
    if num2 > i:
        num2 = i

print(num1, num2)