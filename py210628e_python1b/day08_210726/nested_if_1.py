"""
decision making
branching

4. nested if statement

if
if-else
if-elif-else
"""

# a = 5
# if a>=0:
#     print("+")
# else:
#     print("-")

# after
a = -5
if a >= 0:
    if a > 0:
        print("+")
    else:
        print("0")
else:
    print("-")

# before
a = 5
if a > 0:
    print("+")
elif a == 0:
    if 5>3:
        print()
    else:
        print("0")
else:
    if 9<4:
        print("-")
