"""
string formatting

"""

# example 1
# align to left by default for strings
print("|{:5}|".format("cat"))
print("|{:<5}|".format("cat"))
print("|{:*<5}|".format("cat"))
print()

# example 2
print("|{:>5}|".format("cat"))
print("|{:*>5}|".format("cat"))
print()

# example 3
print("|{:^5}|".format("cat"))
print("|{:^6}|".format("cat"))
print()

# example 4
print("|{:*^5}|".format("cat"))
