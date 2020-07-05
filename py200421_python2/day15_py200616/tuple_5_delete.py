"""
tuple delete
"""

tuple1 = (1, 2, 3, 4, 5, 6)
# del tuple1[0]
# TypeError: 'tuple' object doesn't support item deletion


del tuple1
# NameError: name 'tuple1' is not defined
print(tuple1)

