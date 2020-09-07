"""
logical operator
logical operation

and, or, not
"""

result = 5 > 3 and 3 >2
print(result)

"""
truth table of 'and'

A   B   Q
T   T   T
F   T   F
T   F   F
F   F   F
"""

result = True and False and False
print(result)


result = 5 < 3 or 3 >2
print(result)

"""
truth table of 'or'

A   B   Q
T   T   T
F   T   T
T   F   T
F   F   F
"""
result = True or False or False
print(result)
print()

result = False and False or True
print(result)

result = (False and False) or True
print(result)

result = False and (False or True)
print(result)


result = False or True and False
print(result)


# not
result = not True
print(result)

result = not False
print(result)

result = not 5 > 3
print(result)

result = not 5 > 3 and 3 < 2
print(result)

result = not 5 > 3 or 3 < 2
print(result)
