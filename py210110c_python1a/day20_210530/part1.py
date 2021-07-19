"""
STEM 1401 Python I a
Spring 2021
Solution of Exam
"""

# q17
print("===q17===")
mystr = u'\u00a9 2019 copyrights'
print(mystr)
print()

# q18
print("===q18===")
mystr = "aaa'xxx\"mn\\bb\\nccc"
print(mystr)
print()

# q19
print("===q19===")
print(10==9+True)
print(10==(9+True))  # the same as above
print((10==9)+True)
print()

# q21
print("===q21===")
num = 9
result = isinstance(num, int)
result = isinstance(num, float)
print(result)

# print(isinstance(num, int))


# q22



# q24
print('aaa',end='')
print(' ',end='')
print('bbb',end='')
print(' ',end='')
print('ccc')

print()
print('aaa',' ',end='',sep='')
print('bbb',' ',end='',sep='')
print('ccc')