"""
7/15/2020
Guang Zhu Cui
[Homework]
4 X 4 plate,   Start from A to B
find the route from A to B
"""
print('  ==== The 4x4 plate ====')
print('  _______________________')
print('3 | ---- ---- ---- ---- |')
print('2 | ---- ---- ---- ---- |')
print('1 | ---- ---- ---- ---- |')
print('0 | ---- ---- ---- ---- |')
print('     0    1    2    3    ')
print('Here is a 4x4 plate and I will show you the path from the point A to the point B')
a = 0
b = 0
c = 3
d = 3
print('point A =',(a, b))
print('point B =',(c, d))
print('So here is the path from A to B:')
if a and b == c and d:
    print('The 2 points are at the same place.')
while a != c:
    if a < c:
        print('right (\u2192)')
        a += 1
    if a > c:
        print('left (\u2190)')
        a -= 1
while b != d:
    if b < d:
        print('up (\u2191)')
        b += 1
    if b > d:
        print('down (\u2193)')
        b -= 1

