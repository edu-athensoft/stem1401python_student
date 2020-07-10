"""
operator
logical operator - or

and - keyword
or - keyword
not - keyword
"""

"""
Switch 1.   T     F
Switch 2.   T     F
Light       T     F

Truth Table of or

S1      S2      L
------------------
T       F       T       (case1)
F       T       T       (case2)
F       F       F       (case3)
T       T       T       (case4)
"""

# case 1
s1 = True
s2 = False
light = s1 or s2
print(light)

# case 2
s1 = False
s2 = True
light = s1 or s2
print(light)

# case 3
s1 = False
s2 = False
light = s1 or s2
print(light)

# case 4
s1 = True
s2 = True
light = s1 or s2
print(light)


# whether I would go out for play?
# condition 1.  if I have pocket money, I would go out
# condition 2.  if it is sunny, I would go out
# and
hasMoney = False
isSunny = False
go_out_or_not = hasMoney or isSunny
print("I have money? '{}' and Is it sunny? '{}'; and my decision is go out for play? '{}'".format(hasMoney, isSunny, go_out_or_not))
