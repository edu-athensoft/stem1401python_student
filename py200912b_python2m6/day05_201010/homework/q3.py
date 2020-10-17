"""
3. There are 3 candidates in the election for President in ABC country.
They got voted in every state/province in ABC country.
You are asked to calculate who got the highest vote in the election.

Name		Voted in State1       Voted in State2     Voted in State3
Jason		300			            360			        270
Bill		280			            340			        291
William		350			            310			        324
"""

from collections import Counter

# data from state1
vote_state1 = {
    "Jason" :   300,
    "Bill" :    280,
    "William" : 350
}

# data from state2
vote_state2 = {
    "Jason" :   360,
    "Bill" :    340,
    "William" : 310
}

# data from state2
vote_state3 = {
    "Jason" :   270,
    "Bill" :    291,
    "William" : 324
}

result = Counter(vote_state1) + Counter(vote_state2) + Counter(vote_state3)
print(result)





