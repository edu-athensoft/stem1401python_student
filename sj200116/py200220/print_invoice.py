"""
print out a real invoice
"""

# step 1. to print out document title
print("East Repair Inc.")
print("Invoice")

print("East Repair Inc.                                       Invoice")


print("{:68s} {:10s}".format("East Repair Inc.","Invoice"))
print()

# how to print out the grid line
print("\u250f-----------------\u2533------------------\u2513")
print("|    Item Name    |             50.00|")
print("\u2523-----------------\u254b------------------\u252b")
print("\u2523-----------------\u254b------------------\u252b")
print("\u2517-----------------\u253b------------------\u251b")