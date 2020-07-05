"""
literal_number
integer  2, 8, 16 base to 10 base
"""

# case 1. Integer
i1 = 10
i2 = 100000000
i3 = -9999

# binary integer   starting with 0b
b1  = 0b101     #5
b2  = 0b10000   #16

#   10011100010100101010 => ? on base of 16
b3 = 0b10011100010100101010
# hex()
print(hex(b3))
# bin()
print(bin(9999))

h1 = 0x9c52a
print(h1)

# oct()
print(oct(9999))

print(0b10011100001111)


# case 2. Float
f1 = 1.3
f2 = 0.6666666
f3 = -5.66443


# case 3. Complex
c1 = 1 + 2j
# c1 = 1 + 2i

"""
Homework
1. Octal Integer
octal number
0o,  oO
0b10011100010100101010 -> ?(8)
0x9c52a  -> ?(8)
?(8) -> ?(2)
?(8) -> ?(16)

2. Research
What is a Float number?
"""

