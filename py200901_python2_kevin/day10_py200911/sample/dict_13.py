"""
Python dictionary comprehension
"""

# {1:1, 2:4, 3:9, 4:16}

squares = {x: x*x for x in range(1,5)}
print(squares)


# equivalent
squares = {}
for x in range(1,5):
    squares[x] = x*x
print(squares)



