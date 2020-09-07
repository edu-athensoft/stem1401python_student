"""
number formatting with padding for int and float
"""


#   1
#   2
#   3
#   4
#   5
#   6
#   7
#   8
#   9
#  10
#  11
#  12
#
#  99
# 100

print("{:03d} {}".format(5, 'Mary'))
print("{:03d} {}".format(15, 'Peter'))
print("{:03d} {}".format(105, 'Jack'))
print()

print("{:09.2f} {}".format(5.12, 'Mary'))
print("{:09.2f} {}".format(15.12, 'Peter'))
print("{:09.2f} {}".format(105.12, 'Jack'))

print("{:9.2f} {}".format(5.12, 'Mary'))
print("{:9.2f} {}".format(15.12, 'Peter'))
print("{:9.2f} {}".format(105.12, 'Jack'))