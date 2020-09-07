"""
membership operator

in
not in
"""

words = ['this', 'is', 'my', 'program']
target_word = 'is'
print(target_word in words)

target_word = "that"
print(target_word in words)
print()

# not in
target_word = 'is'
print(target_word not in words)

target_word = 'that'
print(target_word not in words)


# ex
points= ((2,2),(4,3),(3,1))
point = (3,3)
print(point in points)

point = (2,2)
print(point in points)

