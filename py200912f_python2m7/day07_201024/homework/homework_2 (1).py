"""
[Homework]

2. There are 3 candidates in the election for President in ABC country.
They got voted in every state/province in ABC country.
You are asked to calculate who got the highest vote in the election.
Name		Voted in State1       Voted in State2     Voted in State3
Jason		      300			        360			        270
Bill		      280			        340	                291
William		      350			        310			        324
"""

from collections import Counter

dict_votes_1 = {
    "Jason": 300,
    "Bill": 280,
    "William": 350
}

dict_votes_2 = {
    "Jason": 360,
    "Bill": 340,
    "William": 310
}

dict_votes_3 = {
    "Jason": 270,
    "Bill": 291,
    "William": 324
}
"""
# the code underneath is for learning purpose only

for keys, values in dict_votes_1.items():
    print(keys, values)

for keys, values in dict_votes_2.items():
    print(keys, values)

for keys, values in dict_votes_3.items():
    print(keys, values)
"""
# the real code:
# dict
result = dict(Counter(dict_votes_1) + Counter(dict_votes_2) + Counter(dict_votes_3))
print(result)

sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))
the_keys = list(sorted_result.keys())
the_values = list(sorted_result.values())
winner = the_keys[the_values.index(max(sorted_result.values()))]
print(f"The final results sorted from the highest to the lowest score of the election is: {sorted_result}. The winner is: {winner}!")
