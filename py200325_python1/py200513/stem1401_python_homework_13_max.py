"""
Number Formatting Types
"""

# d     Decimal integer
print("{:d}".format(12345))

# c     Corresponding Unicode character
print("{:c}".format(12345))

# b     Binary format
print("{:b}".format(12345))

# o     Octal format
print("{:o}".format(123456789))

# x     Hexadecimal format (lower case)
print("{:x}".format(123456789))

# X     Hexadecimal format (upper case)
print("{:X}".format(123456789))

# n     Same as 'd'.Except it uses current locale setting for number separator
print("{:n}".format(12345))

# e     Exponential notation. (lowercase e)
print("{:e}".format(123456789))

# E     Exponential notation. (uppercase E)
print("{:E}".format(123456789))

# f     Displays fixed point number (Default: 6)
print("{:.2f}".format(1234.56789))

# F     Same as 'f'. Except displays 'inf' as 'INF' and 'nan' as 'NAN'
print("{:.2F}".format(1234.56789))

# g     General format. Rounds number to p significant digits. (Default precision: 6)
print("{:.10g}".format(123456789))
print("{:.10g}".format(123456789123456789))

# G     Same as 'g'. Except switches to 'E' if the number is large
print("{:.10g}".format(123456789123456789))

# %     Percentage. Multiplies by 100 and puts % at the end
print("{:.3%}".format(1234567.89))
print("{:.2%}".format(1234567.89))
print("{:.0%}".format(1234567.89))


