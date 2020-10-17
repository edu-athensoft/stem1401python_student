"""
dictionary Counter
"""


# candidate 1, 2
# vote by state

# candidate1
# A state : 50
# B state : 45
# C state : 70

# candidate2
# A state : 60
# B state : 50
# C state : 40

from collections import Counter

# import collections

# state A
vote_state_a = {
    'c1' : 50,
    'c2' : 60
}

# state B
vote_state_b = {
    'c1' : 45,
    'c2' : 50
}

# state C
vote_state_c = {
    'c1' : 70,
    'c2' : 40
}

# calculate number of ticket for every candidate
result = Counter(vote_state_a) + Counter(vote_state_b) + Counter(vote_state_c)
print(result)

result = dict(result)
print()

# trail
result = Counter(vote_state_a) - Counter(vote_state_b)
print(result)



