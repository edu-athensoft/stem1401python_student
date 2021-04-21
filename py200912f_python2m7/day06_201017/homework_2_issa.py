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

# dict_votes = {
#     "Jason": (300, 360, 270),
#     "Bill": (280, 340, 291),
#     "William": (350, 310, 324)
# }
#
#
# values = dict(dict_votes.values())
#
# print(values[1])
# score_2 = lambda score: score[1][1]
# score_3 = lambda score: score[1][2]
#

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

# dict()
result = dict(Counter(dict_votes_1)+ Counter(dict_votes_2) + Counter(dict_votes_3))
print(result)


# for k,v in dict_votes_1.items():
#     print(k, v)


