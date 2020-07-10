"""
combine boolean literals, comparison expression, logical expression
"""


# case 1.
result = 5 > 12 and 5 < 3
print("5 > 12 and 5 < 3 is",result)

# case 2
result = 5 > 12 or 5 > 3
print("5 > 12 or 5 > 3 is",result)
print()

# case 3
result = 5 < 12 or 5 > 3 and False
print("5 < 12 or 5 > 3 is and False is ",result)

result = 5 < 12 or (5 > 3 and False)
print("5 < 12 or (5 > 3 and False) is ",result)

result = (5 < 12 or 5 > 3) and False
print("(5 < 12 or 5 > 3) and False is ",result)


# game RTS
# cond 1. eliminate all the enemies
# cond 2. destroy all the constructions
# cond 3. escort the specified characters

# difficulty lv 1. easy
"""
cond1. or cond2. or cond3.
"""

# difficulty lv 2. normal
"""
(cond1. and cond2)  or cond3
"""

# difficulty lv3. hard
"""
cond1. and cond2. and cond3.
"""



