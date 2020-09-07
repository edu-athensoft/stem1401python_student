"""
string formatting with format()

padding
"""

# align to left by default
print("|{:5}|".format('cat'))

# align to right
print("|{:>5}|".format('cat'))

# centered
print("|{:^5s}|".format('cat'))
print("|{:^6s}|".format('cat'))

# align to left
print("|{:<5}|".format('cat'))

# padding
print("|{:*^15s}|".format('cat'))
print("|{:=^15s}|".format('cat'))
print("|{:&^15s}|".format('cat'))
print("|{:%^15s}|".format('cat'))
print("|{:c^15s}|".format('cat'))

# truncating strings
print("|{:}|".format('caterpillar'))
print("|{:.3}|".format('caterpillar'))


