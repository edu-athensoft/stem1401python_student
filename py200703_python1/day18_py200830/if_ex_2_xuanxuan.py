"""

"""
a = float(input('Input the first number: '))
b = float(input('Input the second number: '))
c = float(input('Input the third number: '))

strtemp = '{} is the largest number'
if b > a:
    if b > c:
        print(strtemp.format(b))
    else:
        print(strtemp.format(c))
elif a > c:
    print(strtemp.format(a))
else:
    print(strtemp.format(c))
