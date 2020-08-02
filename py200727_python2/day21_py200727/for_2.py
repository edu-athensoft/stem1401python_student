"""
input a number : 10
12 x 1 = 12
12 x 2 = 24
12 x 3 = 36
...
12 x a = 12*a

12 x 10 = 120
12 X 12 = 144


for-loop
string.format()
input()
"""

# num = range(1,int(input("Please enter a number: ")) + 1)
#
# str_temp = "12 x {} = {}"
#
# for a in num:
#     print(str_temp.format(a, 12 * a))
#

# input a number
num = int(input("Please enter a number: "))
num += 1

# generating multiplication table
for i in range(1,num):
    # print(i)
    str_temp = "12 x {} = {}"
    print(str_temp.format(i, 12*i))

