"""
1.Python Program to Display the multiplication Table
Required:
Python for Loop
Python Input, Output and Import
Sample Result:
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
12 x 4 = 48
12 x 5 = 60
12 x 6 = 72
12 x 7 = 84
12 x 8 = 96
12 x 9 = 108
12 x 10 = 120
...
12 x n = ...

"""

# xuanxuan

n = int(input('Enter a number of multiplication table: '))
multiplication = list(range(1,n+1))
strtemp = '12 X {:2} = {:3}'
for x in multiplication:
    print(strtemp.format(x, x * 12))

# lucas
# num = int(input("Which number would you like to display the multiplication table of? "))
#
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)



