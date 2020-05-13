"""
truncate against strings
.3
"""

print("{:.3}".format("caterpillar"))
print("{:.4}".format("caterpillar"))
print("{:.5}".format("caterpillar"))

# and padding
print("|{:5.3}|".format("caterpillar"))
print("|{:>5.3}|".format("caterpillar"))
print("|{:^5.3}|".format("caterpillar"))
