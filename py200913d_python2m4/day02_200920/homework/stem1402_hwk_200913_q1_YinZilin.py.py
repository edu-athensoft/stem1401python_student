"""
quiz 1
My quiz anwsers:
1.a and c
2.a and d
3.b
4.a
5.a
6.a and b
7.a
"""


"""
Homework: forming a triangle with *
"""
# I tried using while loop but i failed
num = 5
row = 0
while row < num:
    star = row + 1
    while star > 0:
        print("*",end=" ")
        star = star - 1
    row = row + 1
print()
print()

print("*")
print("{:3s}{}".format('*','*'))
print("{:3s}{:3s}{}".format('*','*','*'))
print("{:3s}{:3s}{:3s}{}".format('*','*','*','*'))
print("{:3s}{:3s}{:3s}{:3s}{}".format('*','*','*','*','*'))