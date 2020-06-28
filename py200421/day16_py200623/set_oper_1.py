"""
set operation
union()
intersection()
difference()
Symmetric Difference



"""

A = {'card1','card2','card3'}
B = {'card1','card2','card4'}

# question 1. how many kinds of card do the 2 person have?
# A and B have card1 - card4  (4)

result = A | B
print(result)

result = A.union(B)
print("A union B is {}".format(result))
print()

# question 2. how many kinds of card are the common ones they share?
result = A & B
print(result)

result = A.intersection(B)
print("A intersect with B is {}".format(result))
print()


