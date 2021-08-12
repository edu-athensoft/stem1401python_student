"""
if-elif-else statement 2


Syntax

if condition1:
    if-block
elif condition2:
    elif-block
elif condition3:
    elif-block2
...
else:

"""

"""
96-100  A+
93-95   A
90-92   A-
85-89   B+
80-84   B
75-79   B-
66-74   C
60-65   D
0-59    F

input a score, please give the grade accordingly
"""

score = -67
grade = 'INVALID'

if score >=96 and score <=100:
    print('You\'ve got A+')
elif score>=93 and score <=95:
    print('You\'ve got A')
elif score>=90 and score <=92:
    print('You\'ve got A-')
elif score>=85 and score <=89:
    print('You\'ve got B+')
elif score>=80 and score <=84:
    print('You\'ve got B')
elif score>=75 and score <=79:
    print('You\'ve got B-')
elif score>=66 and score <=74:
    print('You\'ve got C')
elif score>=60 and score <=65:
    print('You\'ve got D')
elif score>=0 and score <=59:
    print('You\'ve got F')
else:
    print(grade)


