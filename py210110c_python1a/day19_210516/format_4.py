"""
String formatting

for string

>
^
<   Left aligned (default)
=

"""

str1 = 'cat'

# orginal
print("|{:}".format(str1))
print("|{:5}".format(str1))
print("|{:5}|".format(str1))


# right aligned
print("|{:>5}|".format(str1))

# left aligned
print("|{:<5}|".format(str1))

# center aligned
print("|{:^5}|".format(str1))


# filling and padding char
print("|{:*^5}|".format(str1))
print("|{:=^5}|".format(str1))
print("|{:=^15}|".format(str1))