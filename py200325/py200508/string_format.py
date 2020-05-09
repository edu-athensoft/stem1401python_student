"""
string template
template is a string with placeholders {}

template.format(p0, p1, ..., k0=v0, k1=v1, ...)

p denotes for positional,  positional argument
k key , named argument
v value, value of named argument

fact 1.
p0 - pn  0..n
k0=v0 - kn=vn   0..m

fact 2.
all positional argument should stay before named argument (k-v pairs)
"""
a = 1
b = 2
c = 3
x1 = 'aaa'
y1 = 'bbb'
z1 = 'ccc'

print("{} {} {}  {x}  {y} {z}".format(a,b,c, x=x1, y=y1, z=z1))

# print("{} {} {}  {x}  {y} {z}".format(x=x1, y=y1, z=z1, a, b,c ))

# print("{} {} {}  {x}  {y} {z}".format(a,c, x=x1, y=y1, z=z1, b))

