"""
String formatting
alignment of numbers

<   Left aligned
^   Center aligned
>   Right aligned  (default)
=   Forces the sign (+ / -) to the leftmost position

"""

# original example
print("The number is |{:5d}|".format(123))

# right aligned
print("The number is |{:<5d}|".format(123))

# centered
print("The number is |{:^5d}|".format(123))
print("The number is |{:6d}|".format(123))
print("The number is |{:^6d}|".format(123))
print("The number is |{:^8d}|".format(123))

# right aligned
print("The number is |{:>5d}|".format(123))


#
print("The number is |{:+7d}|".format(123))
print("The number is |{:=+7d}|".format(123))

print("The number is |{:+7d}|".format(-123))
print("The number is |{:=+7d}|".format(-123))