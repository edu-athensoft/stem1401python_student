"""
literal
Literal is raw data given in variable or constant

1. numeric literals
2. string literals
3. boolean literals
4. special literals
5. literal collections

"""

# a = 1
# a = 'abc'
# a = True

# 1.1 integer number

# bin(), hex(), oct()

# 1.1.1
d1 = 10
d2 = 123

"""
binary  decimal hex
0000    0       0
0001    1       1
0010    2       2
0011    3       3
0100    4       4
0101    5       5
0110    6       6
0111    7       7
1000    8       8
1001    9       9
1010    10      A
1011    11      B
1100    12      C
1101    13      D
1110    14      E
1111    15      F
"""
b0 = 0b0
b1 = 0b1
b2 = 0b10
b10 = 0b1010
print(b0)
print(b1)
print(b2)
print(b10)
print()

"""
binary  decimal octal
000    0       0
001    1       1
010    2       2
011    3       3
100    4       4
101    5       5
110    6       6
111    7       7
"""

# 1.1.2 octal
o1 = 0o2345
print(o1)

o2 = 0o10
print(o2)
print()

# 1.1.3 hex, hexadecimal
x1 = 0x1
x2 = 0x10
x3 = 0x100
x4 = 0x1000
print(x1, x2, x3, x4)
print()

print("1234 = binary:", bin(1234))
print("789 = binary:", bin(789))
# 1100010101

print("1234 = hex:", hex(1234))
print("1234 = oct:", oct(1234))
print()


# 1.2 floating number
f1 = 1.23
f2 = -1.23
print(f1, f2)

# scientific notation
f3 = 0.0000000000000000123
print(f3)
print(1.23e-17)

f4 = 1230000000000000
print(f4)
print(1.23e15)


# 1.3 complex
n = 1 + 3j
print(n)
print(n.real, n.imag)







