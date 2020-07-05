"""
Number Formatting Types
"""

# Decimal Integer
# It gives the number of position the output will be
a = 12
print("{:5d}".format(a))

# Corresponding Unicode character
# It gives the unicode value of the integer
b = 33
print("{:c}".format(b))

# Binary format
# It gives the binary value of the integer
c = 16
print("{:b}".format(c))

# Octal format
# It gives the octal va;ue of the integer
d = 34
print("{:o}".format(d))

# Hexadecimal format
# It gives the hexadecimal value of the integer
e = 15
print("{:x}".format(e))

# Exponential notation
# It puts a . between the first and second digit of the value (I'm not really sure)
f = 24
print("{:.2e}".format(f))

# Displays fixed point number
# It gives the number of decimal digits the number will display
g = 35.4
print("{:.4f}".format(g))

# General format
# It rounds the number
h = 34.4
print("{:.2g}".format(h))

# Percentage
i = 0.34
print("{:.0%}".format(i))
