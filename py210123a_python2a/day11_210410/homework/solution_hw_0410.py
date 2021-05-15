"""
solution

['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
"""

# 1.

result = [i**2 for i in range(1,101) if i %2 == 0]
print(result)

# 2.

string1 = 'ABC'
string2 = 'XYZ'

result = [c1+c2 for c1 in string1 for c2 in string2]
print(result)