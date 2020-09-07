"""
number formatting with alignment

<
^   centered
>
=   forces the sign(+/-) to the leftmost position
"""

# align to right by default
print("|{:5d}|".format(12))
print("|{:6d}|".format(12))

# centered
print("|{:^6d}|".format(12))

# left
print("|{:<6d}|".format(12))

# right
print("|{:>6d}|".format(12))

# leftmost for sign
print("|{:=6d}|".format(-12))
print("|{:=+6d}|".format(+12))