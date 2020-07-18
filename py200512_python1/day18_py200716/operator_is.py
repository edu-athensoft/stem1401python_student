"""
test if two objects are the same

identity operator
is, is not

keywords: is, not

== means to test if two objects have the same value
is means to test if two objects are identical
"""

# case 1.
s1 = 'abc'
s2 = 'bcd'

print("s1 == s2 ? ",s1==s2)
print()

# case 2.
s3 = 'xyz'
s4 = 'xyz'

print("s3 == s4 ?", s3==s4)
print()

# case 3.
s1 = 'abc'
s2 = 'bcd'
print("s1 is s2 ? ",s1 is s2)
print()

# case 4.
s3 = 'xyz'
s4 = 'xyz'

print("s3 is s4 ? ",s3 is s4)
