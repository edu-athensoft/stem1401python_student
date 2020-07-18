"""
7/13/2020
Ze Yue Li
[Homework]
4 X 4 plate,   Start from A to B
find the route from A to B
"""
from random import randint

bX = int(input("Input the ending X"))
bY = int(input("Input the ending Y"))
posX = int(input("Input the starting Y"))
posY = int(input("Input the starting X"))
list1 = []
print(posX, posY)
a = str(posX)+str(posY)
list1.append(a)
while bX != posX or bY != posY:
    if posX != bX and bY != posY:
        if randint(1,2) == 1:
            if posX < bX:
                posX += 1
            else:
                posX -= 1
        else:
            if posY < bY:
                posY += 1
            else:
                posY -= 1
    else:
        if posX == bX:
            if posY < bY:
                posY += 1
            else:
                posY -= 1
        else:
            if posX < bX:
                posX += 1
            else:
                posX -= 1
    print('(',posX,',',posY,')')
    a = str(posX)+str(posY)
    list1.append(a)
a = str(bX)+str(bY)
list1.append(a)
print(list1)
if '30' in list1:
    aa = 'x'
else:
    aa = '_'
if '31' in list1:
    ab = 'x'
else:
    ab = '_'
if '32' in list1:
    ac = 'x'
else:
    ac = '_'
if '33' in list1:
    ad = 'x'
else:
    ad = '_'
if '20' in list1:
    ba = 'x'
else:
    ba = '_'
if '21' in list1:
    bb = 'x'
else:
    bb = '_'
if '22' in list1:
    bc = 'x'
else:
    bc = '_'
if '23' in list1:
    bd = 'x'
else:
    bd = '_'
if '10' in list1:
    ca = 'x'
else:
    ca = '_'
if '11' in list1:
    cb = 'x'
else:
    cb = '_'
if '12' in list1:
    cc = 'x'
else:
    cc = '_'
if '13' in list1:
    cd = 'x'
else:
    cd = '_'
if '00' in list1:
    da = 'x'
else:
    da = '_'
if '01' in list1:
    db = 'x'
else:
    db = '_'
if '02' in list1:
    dc = 'x'
else:
    dc = '_'
if '03' in list1:
    dd = 'x'
else:
    dd = '_'
print('| {} | {} | {} | {} |'.format(aa,ab,ac,ad))
print('| {} | {} | {} | {} |'.format(ba,bb,bc,bd))
print('| {} | {} | {} | {} |'.format(ca,cb,cc,cd))
print('| {} | {} | {} | {} |'.format(da,db,dc,dd))



